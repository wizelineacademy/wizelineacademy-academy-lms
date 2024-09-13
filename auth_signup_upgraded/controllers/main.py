# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

import logging
import werkzeug
from werkzeug.urls import url_encode


from odoo.addons.auth_signup.models.res_users import SignupError
from odoo.exceptions import UserError

from odoo import http, _
from odoo.addons.auth_signup.controllers.main import AuthSignupHome
from odoo.addons.web.controllers.home import ensure_db, LOGIN_SUCCESSFUL_PARAMS

from odoo.http import request

_logger = logging.getLogger(__name__)

LOGIN_SUCCESSFUL_PARAMS.add('account_created')

class RedirectedSignup(AuthSignupHome):
    
    # controller for 
    @http.route()
    def web_login(self, *args, **kw):
        ensure_db()
        response = super().web_login(*args, **kw)
        response.qcontext.update(self.get_auth_signup_config())
        if request.session.uid:
            if request.httprequest.method == 'GET' and request.params.get('redirect'):
                # Redirect if already logged in and redirect param is present
                return request.redirect(request.params.get('redirect'))
            # Add message for non-internal user account without redirect if account was just created
            if response.location == '/web/login_successful' and kw.get('confirm_password'):
                return request.redirect_query('/web/login_successful', query={'account_created': True})
            # Path for redirecting to home page after successfull login
            return request.redirect("/")
        return response
    
    # controller for user sign in
    # these two methods handle the user inputs for the login
    def get_auth_signup_qcontext(self):
        qcontext = super(RedirectedSignup, self).get_auth_signup_qcontext()
        """ Shared helper returning the rendering context for signup and reset password """
        other_fields = {k: v for (k, v) in request.params.items() if k in ['last_name', 'city', 'phone', 'gender', 'linkedIn', 'recruitment', 'country_id', 'policy_agreement']}
        qcontext.update(other_fields)
        return qcontext
    
    def _prepare_signup_values(self, qcontext):
        values = super(RedirectedSignup, self)._prepare_signup_values(qcontext)
        values.update({ key: qcontext.get(key) for key in ('last_name', 'city', 'phone', 'gender', 'linkedIn', 'recruitment', 'country_id', 'policy_agreement') })
        return values
    
    # this method allows for the countries dropdown to work
    @http.route('/web/signup', type='http', auth='public', website=True, sitemap=False)
    def web_auth_signup(self, *args, **kw):
        
        # these two lines allow for country to work
        qcontext = self.get_auth_signup_qcontext()
        qcontext['countries'] = http.request.env['res.country'].sudo().search([])
        
        # this is part of the original method of web_auth_signup
        if not qcontext.get('token') and not qcontext.get('signup_enabled'):
            raise werkzeug.exceptions.NotFound()

        if 'error' not in qcontext and request.httprequest.method == 'POST':
            try:
                self.do_signup(qcontext)

                # Set user to public if they were not signed in by do_signup
                # (mfa enabled)
                if request.session.uid is None:
                    public_user = request.env.ref('base.public_user')
                    request.update_env(user=public_user)

                # Send an account creation confirmation email
                User = request.env['res.users']
                user_sudo = User.sudo().search(
                    User._get_login_domain(qcontext.get('login')), order=User._get_login_order(), limit=1
                )
                template = request.env.ref('auth_signup.mail_template_user_signup_account_created', raise_if_not_found=False)
                if user_sudo and template:
                    template.sudo().send_mail(user_sudo.id, force_send=True)
                return self.web_login(*args, **kw)
            except UserError as e:
                qcontext['error'] = e.args[0]
            except (SignupError, AssertionError) as e:
                if request.env["res.users"].sudo().search([("login", "=", qcontext.get("login"))]):
                    qcontext["error"] = _("Another user is already registered using this email address.")
                else:
                    _logger.warning("%s", e)
                    qcontext['error'] = _("Could not create a new account.") + "\n" + str(e)

        elif 'signup_email' in qcontext:
            user = request.env['res.users'].sudo().search([('email', '=', qcontext.get('signup_email')), ('state', '!=', 'new')], limit=1)
            if user:
                return request.redirect('/web/login?%s' % url_encode({'login': user.login, 'redirect': '/web'}))

        response = request.render('auth_signup.signup', qcontext)
        response.headers['X-Frame-Options'] = 'SAMEORIGIN'
        response.headers['Content-Security-Policy'] = "frame-ancestors 'self'"
        return response
    

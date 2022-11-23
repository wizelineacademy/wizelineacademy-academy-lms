"""
import webbrowser
from odoo import models, api

class ResUserTalent(models.Model):
    _inherit = 'res.users'
    @api.model
    def _auth_oauth_signin(self, provider, validation, params):
        login = super(ResUserTalent, self)._auth_oauth_signin(provider, validation, params)
        if login != "nicolashh.1305@gmail.com":
            webbrowser.open("https://auth.talent.wizeline.com/")
        return login
"""

# -*- coding: utf-8 -*-
# Part of BrowseInfo. See LICENSE file for full copyright and licensing details.

from odoo import SUPERUSER_ID
import odoo.addons.website_crm_partner_assign.controllers.main as website_partner_main
import werkzeug.urls
import werkzeug.wrappers
import json
import logging
from werkzeug.exceptions import Forbidden

from odoo import http, tools, _
from odoo.http import request
from odoo.addons.base.models.ir_qweb_fields import nl2br
from odoo.addons.http_routing.models.ir_http import slug
from odoo.addons.website.controllers.main import QueryURL
from odoo.exceptions import ValidationError


class website_partner_rating_comments( website_partner_main.WebsiteCrmPartnerAssign ):
    """ This method is overloaded for to add messaege_rate and short_description
    in product.template"""
    @http.route(['/partners/partner/comment/<int:partner_id>'], type='http', auth="public", methods=['POST'], website=True)
    def partner_rating( self, partner_id, **post ):
        partner_obj = request.env['res.partner'].browse(partner_id)
        if post.get( 'comment' ):
            message_id1 = partner_obj.sudo().message_post(
                body=post.get( 'comment' ),
                message_type='comment',
                subtype_xmlid='mail.mt_comment',
             )

            review = post.get('review')
            short_description = post.get( 'short_description' )
            mail_message1 = request.env['mail.message']
            message_id1.write({'message_rate':review, 
            					'short_description':short_description, 
            					'website_message':True} )
        return werkzeug.utils.redirect( request.httprequest.referrer + "#comments" )
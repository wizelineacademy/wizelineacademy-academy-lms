# -*- coding: utf-8 -*-
# Part of BrowseInfo. See LICENSE file for full copyright and licensing details. 

from odoo import models, fields, api, _

class mailmessage(models.Model):
    _inherit='mail.message'
    
    message_rate = fields.Integer( 'Message Rating' )
    short_description = fields.Char( 'Short Description' )
    website_message = fields.Boolean( 'Is Website Message', default=False )

 
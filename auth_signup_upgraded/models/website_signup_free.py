from odoo import models, fields
from odoo import api

class WebsiteSignupFree(models.Model):
    _inherit = 'website'
    
    auth_signup_uninvited = fields.Selection([
        ('b2b', 'On invitation'),
        ('b2c', 'Free sign up'),
    ], string='Customer Account', default='b2c')
    
    def init(self):
        super(WebsiteSignupFree, self).init()
        websites = self.search([])
        websites.write({'auth_signup_uninvited': 'b2c'})
        
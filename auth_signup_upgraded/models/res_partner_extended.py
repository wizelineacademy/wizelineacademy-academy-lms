from odoo import models, fields
from odoo import api
from odoo.exceptions import UserError
import re

class ResPartnerExtended(models.Model):
    _inherit = 'res.partner'
    
    last_name = fields.Char(string="Last Name")
    gender = fields.Char(string="Gender")
    linkedIn = fields.Char(string="Linkedin Profile URL")
    recruitment = fields.Selection([('yes','Yes'),('no','No')],string="")
    policy_agreement = fields.Boolean(string="Privacy Policy Agreement", default=False)
    
    @api.constrains('email')
    def _validate_email(self):
        regex = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
        for rec in self:
            if rec.email and re.match(regex,rec.email) == None:
                raise UserError("Please enter a correct email address")
    
    @api.constrains('phone')
    def _validate_phone(self):
        for rec in self:
            if len(rec.phone) < 10 or rec.phone.isnumeric() == False:
                raise UserError("Please enter a valid phone number")
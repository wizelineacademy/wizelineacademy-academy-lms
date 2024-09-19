from odoo import models, fields

class ResPartner(models.Model):
    _inherit = 'res.partner'

    is_lecturer = fields.Boolean(string='Lecturer', default=False)
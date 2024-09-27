from odoo import models, fields

class SlideChannelExtended(models.Model):
    _inherit = 'slide.channel'


    lecturers = fields.Many2many('res.partner', string='Lecturers', help='Contacts affiliated as lecturers for this course.', domain=[('is_lecturer', '=', True)], required=False)
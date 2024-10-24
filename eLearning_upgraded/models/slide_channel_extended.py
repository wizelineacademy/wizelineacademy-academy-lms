from odoo import models, fields

class SlideChannelExtended(models.Model):
    _inherit = 'slide.channel'

    who_should_take = fields.Html(string='Who should take this course?', help='This field is used to describe the target audience for this course.', required=False)
    lecturers = fields.Many2many('res.partner', string='Lecturers', help='Contacts affiliated as lecturers for this course.', domain=[('is_lecturer', '=', True)], required=False)
    language_id = fields.Many2one('res.lang', string="Language",  help="This field is used to define the language for this course.", required=False)
    language_name = fields.Char(string="Language Name", compute='_compute_language_name')

    def _compute_language_name(self):
        for record in self:
            record.language_name = record.language_id.name if record.language_id else ''
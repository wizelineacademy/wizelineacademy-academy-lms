from odoo import models, fields

class SlideChannelExtended(models.Model):
    _inherit = 'slide.channel'

    who_should_take = fields.Html(string='Who should take this course?', help='This field is used to describe the target audience for this course.', required=False)
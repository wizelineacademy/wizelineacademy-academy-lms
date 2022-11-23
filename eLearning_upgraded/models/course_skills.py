from odoo import models, fields

class CourseSkills(models.Model):
    _inherit = 'slide.channel'

    skill_ids = fields.Many2many('slide.skill.tag', string='Skills', help='Specify the skills the student is going to acquire')
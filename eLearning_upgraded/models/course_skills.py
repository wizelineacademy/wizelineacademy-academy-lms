from odoo import models, fields

class CourseSkills(models.Model):
    _inherit = 'slide.channel'

    skill_ids = fields.Many2many('slide.skill.tag', string='Skills', help='Specify the skills the student is going to acquire')
    skill_names = fields.Char(string="Skill Names", compute='_compute_skill_names')

    def _compute_skill_names(self):
        for record in self:
            record.skill_names = ', '.join(record.skill_ids.mapped('name'))
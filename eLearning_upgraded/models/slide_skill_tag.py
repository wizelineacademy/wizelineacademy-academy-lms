from odoo import models, fields
from random import randint
#from google.cloud import bigquery


class SlideChannelTag(models.Model):
    _name = 'slide.skill.tag'
    _description = 'Channel/Course Skill'
    _order = 'sequence asc'

    name = fields.Char('Name', required=True, translate=True, readonly=True)
#   external_id = fields.Char('External ID', required=True, translate=True, readonly=True)
    sequence = fields.Integer('Sequence', default=10, index=True, required=True)
    color = fields.Integer(
        string='Color Index', default=lambda self: randint(1, 11),
        help="Tag color used in both backend and website. No color means no display in kanban or front-end, to distinguish internal tags from public categorization tags")
    
    # Update the skills, this function is called automatically every week 
    def update_skills(self):
        #client = bigquery.Client()

        #query = """
        #    SELECT name
        #    FROM `wizelake-non-prod.wizeline_os.skills`
        #   """
        #query_job = client.query(query)  # Make an API request.


        skills_list = ['Sequelize', 'Haskell', 'Jest', 'Rust', 'Grunt', 'Gulp', 'Python', 'C++'] #skill list in BigQuery
        #for row in query_job:
            # Row values can be accessed by field name or index.
        #    skill_list.append(row[0])
        for skill in skills_list:
            skill_vals = {
                'name': skill
                #,'external_id': skill['external_id']
                # 'name': skill['name']
            }
            #course_skill_id = self.env['slide.skill.tag].search([('external_id', '=', skill['external_id'])])
            course_skill_id = self.env['slide.skill.tag'].search([('name', '=', skill)])
            if not len(course_skill_id):
                self.env['slide.skill.tag'].create(skill_vals)

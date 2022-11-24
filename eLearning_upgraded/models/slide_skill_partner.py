from odoo import models, fields, api
import csv, datetime, os

class CourseStudentSkills(models.Model):
    _inherit = 'slide.channel.partner'

    student_name = fields.Char(related='partner_id.name', readonly=True)
    course_skills = fields.Many2many(related='channel_id.skill_ids')

    
    def export_students(self):
        student_list = []
        save_path = 'src/user/exports/'
        try:
            os.mkdir(save_path)
        except FileExistsError as error:
            print(error)
            
        dt = datetime.datetime.today()
        date = f'_{dt.day}_{dt.month}_{dt.year}'

        students = self.env['slide.channel.partner'].search_read([], {
            'channel_id','student_name','partner_email', 'course_skills', 'create_date', 'write_date', 'completion'} )

        for student in students:
            if len(student['course_skills']):
                for skill in student['course_skills']:
                    # Find and assign the skill name using the ID 
                    vals = [student['channel_id'][1], student['student_name'], student['partner_email']]
                    skill_vals = self.env['slide.skill.tag'].search_read([('id', '=', skill)])
                    skill_name = skill_vals[0]['name']

                    if student['course_skills'].index(skill) != 0:
                        student_list.append(['','','', skill_name, '', '', ''])
                    else:
                        vals.extend([skill_name, student['create_date'], student['write_date'], student['completion']])
                        student_list.append(vals)

            else:
                vals = [student['channel_id'][1], student['student_name'], student['partner_email'], '', student['create_date'], student['write_date'], student['completion']]
                student_list.append(vals)

        with open(save_path + f'exported_students{date}.csv', 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(['course', 'name', 'email', 'skills', 'enrolled', 'last_action', 'progress'])
            writer.writerows(student_list)

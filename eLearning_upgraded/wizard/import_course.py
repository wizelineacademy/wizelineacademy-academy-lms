from odoo import models, fields, api
import requests

class ImportCourseWizard(models.TransientModel):
    _name = "import.course.wizard"
    _description = "Import course wizard"

    document_id = fields.Char(string = 'Document link', required = True)
    def action_import_course(self):
        if 'docs.google.com' in self.document_id and self.document_id.split('/')[-2]:
            doc_id = self.document_id.split('/')[-2]
            try:
                r = requests.get(f'http://127.0.0.1:5000/course_import/{doc_id}')
                return {
                    'type': 'ir.actions.client',
                    'tag': 'display_notification',
                    'params': {
                        'message': 'Creating course',
                        'type': 'success',
                        'sticky': False
                    }
                }
            except requests.exceptions.RequestException as err:
                errorMessage = err 
                return {
                    'type': 'ir.actions.client',
                    'tag': 'display_notification',
                    'params': {
                        'message': errorMessage,
                        'type': 'danger',
                        'sticky': True
                    }
                }
        else:
            return {
                'type': 'ir.actions.client',
                'tag': 'display_notification',
                'params': {
                    'message': 'Invalid Document link',
                    'type': 'danger',
                    'sticky': False
                }
            }

    
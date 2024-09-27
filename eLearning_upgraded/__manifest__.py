{
    'name': "eLearning_upgraded",
    'version': '1.0.1',
    'author': "systemBlue",
    'summary': 'Import courses & add skills',
    'category': 'Website',
    'description': """
    Upgrades and changes to the eLearning module
    """,
    'company': 'systemBlue',
    'website' : 'https://github.com/oszac/Sistemas-de-Software/wiki',
    'depends' : ['website_slides', 'auth_oauth', 'auth_signup_upgraded'],
    'data' : [
        'security/ir.model.access.csv',
        'wizard/import_course_view.xml',
        'views/course_skills_view.xml',
        'views/menu_import_view.xml',
        'views/student_skills_view.xml',
        'views/course_audience_view.xml',
        'views/website_slides_templates_homepage.xml',
        'data/skills_data.xml'
    ],
    'license': 'LGPL-3',
}
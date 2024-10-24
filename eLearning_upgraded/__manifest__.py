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
        'views/website_slides_templates_homepage.xml',
        'views/website_slides_course_main_template.xml',
        'views/website_slides_course_widgets_template.xml',
        'views/website_slides_courses_all.xml',
        'views/course_language_view.xml',
        'views/course_audience_view.xml',
        'views/course_main_lecturers_tab.xml',
        'data/skills_data.xml'
    ],
    'assets': {
        'web.assets_frontend': [
            "eLearning_upgraded/static/src/js/website_slides_tab_actions.js",
        ],
    },
    'license': 'LGPL-3',
}
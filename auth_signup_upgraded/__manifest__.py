{
    'name': "authentication_tools",
    'version': '1.0.0',
    'author': "no one",
    'summary': 'redirect to webpage after login',
    'category': 'Website',
    'description': """
    redirect to webpage after login
    """,
    'company': 'no one',
    'website' : 'https://github.com/oszac/Sistemas-de-Software/wiki',
    'depends' : ['website','auth_signup','portal', 'base', 'mail', 'web', 'auth_oauth'],
    'data' : [
        'views/big_button_sign_in_view.xml',
        'views/extended_signup_view.xml',
        'security/ir.model.access.csv',
        'views/website_main_page_view.xml',
        'views/extended_login_view.xml',
        'views/partner_is_lecturer_view.xml',
    ],
    'installable': True,
    'application': False,
    'license': 'LGPL-3',
}
{
    'name': 'Theme Common',
    'summary': 'Snippets Library',
    'description': 'Snippets library containing snippets to be styled in themes.',
    'category': 'Hidden',
    'version': '1.1',
    'depends': ['website'],
    'data': [
        'data/data.xml',
        'views/old_snippets/s_column.xml',
        'views/old_snippets/s_page_header.xml',
        'views/old_snippets/s_three_columns_circle.xml',
    ],
    'assets': {
        'web._assets_primary_variables': [
            "theme_bewise/static/src/scss/primary_variables.scss",
        ],
    },
    'application': False,
    'license': 'LGPL-3',
}

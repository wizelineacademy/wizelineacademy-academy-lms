# -*- coding: utf-8 -*-
# Part of BrowseInfo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Website Customer Review',
    'version': '16.0.0.1',
    'category': 'Website',
    'license':'OPL-1',
    'summary': 'Website Customet/Partner Rating',
    'description': """
        You can see reviews details with Reviewer name, Rating, Date, Short & Long Description.User can submit their review only when 
    they are logged in. If the user is not logged in, then the system will provide link to login page and once after login user will
    straight away redirected to the partner page.
        You can publish/unpublish reviews from front end website page. For that you must be logged in as Administrator.
        You will able to see Avg. Rating and No. of reviews link at the top of partner detail page in website. By clicking on that you will redirect to reviews list.

        """,
    'author': 'BrowseInfo',
    'website': 'https://www.browseinfo.com',
    'license':'OPL-1',
    'depends': ['website','website_crm_partner_assign','website_partner'],
    'installable': True,
    'data': [
        'data/data.xml',
        'views/template.xml',
        'views/mail_message_view.xml',
    ],
    'assets': {
        'web.assets_frontend': [
          'website_partner_rating/static/src/scss/partner_rating.css',
          'website_partner_rating/static/src/js/comment_priority.js',
        ],
    
        'web.assets_qweb': [
        ],
    },
    'application': True,
    "live_test_url":'https://youtu.be/Dce_ycCQAzI',
    "images":['static/description/Banner.gif'],
}


# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:

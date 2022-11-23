from odoo.tests import common
from odoo.addons.mail.tests.common import mail_new_test_user, MockEmail


class SlidesCaseUpgraded(common.TransactionCase, MockEmail):

    @classmethod
    def setUpClass(cls):
        super(SlidesCaseUpgraded, cls).setUpClass()
        
        # Create admin credentials
        cls.user_officer = mail_new_test_user(
            cls.env, name='New Officer', login='user_officer', email='officer@example.com',
            groups='base.group_user,website_slides.group_website_slides_officer'
        )

        cls.user_manager = mail_new_test_user(
            cls.env, name='New Manager', login='user_manager', email='manager@example.com',
            groups='base.group_user,website_slides.group_website_slides_manager'
        )

        cls.user_emp = mail_new_test_user(
            cls.env, name='New Employee', login='user_emp', email='employee@example.com',
            groups='base.group_user'
        )

        cls.user_portal = mail_new_test_user(
            cls.env, name='New Portal User', login='user_portal', email='portal@example.com',
            groups='base.group_portal'
        )

        # Create users
        cls.customer = cls.env['res.partner'].create({
            'name': 'Test user',
            'email': 'user@example.com',
        })
        cls.customer_2 = cls.env['res.partner'].create({
            'name': 'New test user',
            'email': 'testuser@example.com',
        })

        # Create skills
        cls.skill_1 = cls.env['slide.skill.tag'].with_user(cls.user_officer).create({
            'name': 'New skill'
        })
        # Error, skill names are unique
        cls.skill_2 = cls.env['slide.skill.tag'].with_user(cls.user_officer).create({
            'name': 'New skill'
        })
        cls.skill_3 = cls.env['slide.skill.tag'].with_user(cls.user_officer).create({
            'name': 'Brand New skill'
        })
        # Error, wrong field for skill model
        cls.skill_4 = cls.env['slide.skill.tag'].with_user(cls.user_officer).create({
            'skill_name': 'Error'
        })
        # Create course with skills
        cls.channel = cls.env['slide.channel'].with_user(cls.user_officer).create({
            'name': 'Test Channel',
            'channel_type': 'documentation',
            'promote_strategy': 'most_voted',
            'enroll': 'public',
            'visibility': 'public',
            'is_published': True,
            'skill_ids': [cls.skill_1.id, cls.skill_3.id]
        })
        # Create student with skills and name
        cls.student_1 = cls.env['slide.channel.partner'].with_user(cls.user_officer).create({
            'channel_id': cls.channel.id,
            'partner_id': cls.customer.id,
            'student_name' : cls.customer.name,
            'course_skills' : cls.channel.skill_ids
        })
        # Create student with name
        cls.student_2 = cls.env['slide.channel.partner'].with_user(cls.user_officer).create({
            'channel_id': cls.channel.id,
            'partner_id': cls.customer_2.id,
            'course_skills' : cls.channel.skill_ids
        })
        # Create course content
        cls.slide = cls.env['slide.slide'].with_user(cls.user_officer).create({
            'name': 'How To Cook Humans',
            'channel_id': cls.channel.id,
            'slide_type': 'presentation',
            'is_published': True,
            'completion_time': 2.0,
            'sequence': 1,
        })
        cls.category = cls.env['slide.slide'].with_user(cls.user_officer).create({
            'name': 'Cooking Tips for Humans',
            'channel_id': cls.channel.id,
            'is_category': True,
            'is_published': True,
            'sequence': 2,
        })
        cls.slide_2 = cls.env['slide.slide'].with_user(cls.user_officer).create({
            'name': 'How To Cook For Humans',
            'channel_id': cls.channel.id,
            'slide_type': 'presentation',
            'is_published': True,
            'completion_time': 3.0,
            'sequence': 3,
        })
        cls.slide_3 = cls.env['slide.slide'].with_user(cls.user_officer).create({
            'name': 'How To Cook Humans For Humans',
            'channel_id': cls.channel.id,
            'slide_type': 'document',
            'is_published': True,
            'completion_time': 1.5,
            'sequence': 4,
            'quiz_first_attempt_reward': 42,
        })

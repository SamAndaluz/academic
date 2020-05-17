# -*- coding: utf-8 -*-
# Part of OpenEduCat. See LICENSE file for full copyright & licensing details.

##############################################################################
#
#    Tech-Receptives Solutions Pvt. Ltd.
#    Copyright (C) 2009-TODAY Tech Receptives(<http://www.techreceptives.com>).
#
##############################################################################

from odoo.tests import common, TransactionCase
from ..controllers import onboard, main
from odoo.addons.website.tools import MockRequest
from odoo.http import request


class TestCoreCommon(common.SavepointCase):
    def setUp(self):
        super(TestCoreCommon, self).setUp()
        self.op_subject = self.env['op.subject']
        self.res_company = self.env['res.company']
        self.op_faculty = self.env['op.faculty']
        self.op_course = self.env['op.course']
        self.op_batch = self.env['op.batch']
        self.wizard_badge = self.env['op.badge.student.wizard']


class CoreController(TransactionCase):

    def setUp(self):
        super().setUp()


class TestCoreController(CoreController):

    def setUp(self):
        super(TestCoreController, self).setUp()

    def test_case_1_onboard(self):
        self.onboard_controller = onboard.OnboardingController()

        with MockRequest(self.env):
            self.core_onboard = self.onboard_controller.\
                openeducat_core_enterprise_onboarding_panel()

    def test_case_1_main(self):
        self.core_main_controller = main.StudentPortal()
        with MockRequest(self.env):
            student = request.env.user
            self.main_controller = self.\
                core_main_controller.check_access_role(student)
            self.main_controller = self.\
                core_main_controller.get_student(student_id=None)
            self.main_controller = self.\
                core_main_controller.get_student(student_id=student.id)

    def test_case_2_main_OpenEduCatController(self):
        self.core_main_controller = main.OpenEduCatController()

        with MockRequest(self.env):
            self.main_controller = self.\
                core_main_controller.compute_main_dashboard_data()
            self.main_controller = self.\
                core_main_controller.fetch_openeducat_batches()
            self.main_controller = self.\
                core_main_controller.compute_openeducat_batch_graph(batch_id=None)
            course_id = self.env.ref('openeducat_core.op_course_2')
            self.main_controller = self.\
                core_main_controller.get_course_data(course_id=str(course_id.id))

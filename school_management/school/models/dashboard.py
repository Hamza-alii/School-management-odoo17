from odoo import models, fields, api

class Dashboard(models.Model):
    _name = 'school.dashboard'
    _description = 'School Dashboard'

    name = fields.Char(string='Dashboard Name', default='School Dashboard')

    total_students = fields.Integer(string='Total Students', compute='_compute_dashboard_stats')
    total_classes = fields.Integer(string='Total Classes', compute='_compute_dashboard_stats')
    total_teachers = fields.Integer(string='Total Teachers', compute='_compute_dashboard_stats')
    total_courses = fields.Integer(string='Total Courses', compute='_compute_dashboard_stats')
    attendance_percentage = fields.Float(string='Attendance Percentage', compute='_compute_dashboard_stats')

    def _compute_dashboard_stats(self):
        self.total_students = self.env['school.student'].search_count([])
        self.total_classes = self.env['school.class'].search_count([])
        self.total_teachers = self.env['school.teacher'].search_count([])
        self.total_courses = self.env['school.course'].search_count([])

        total_attendance = self.env['school.attendance'].search_count([])
        total_absent = self.env['school.attendance'].search_count([('status', '=', 'absent')])

        if total_attendance > 0:
            self.attendance_percentage = 100 - (total_absent / total_attendance) * 100
        else:
            self.attendance_percentage = 0.0

    @api.model
    def action_view_model(self, model_name, name):
        return {
            'type': 'ir.actions.act_window',
            'name': name,
            'res_model': model_name,
            'view_mode': 'tree,form',
        }

    def action_students(self):
        return self.action_view_model('school.student', 'All Students')

    def action_classes(self):
        return self.action_view_model('school.class', 'All Classes')

    def action_teachers(self):
        return self.action_view_model('school.teacher', 'All Teachers')

    def action_courses(self):
        return self.action_view_model('school.course', 'All Courses')

    def action_attendance(self):
        return self.action_view_model('school.attendance', 'Attendance Records')

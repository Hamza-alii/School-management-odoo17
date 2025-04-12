from odoo import models, fields

class Attendance(models.Model):
    _name = 'school.attendance'
    _description = 'Attendance'

    student_id = fields.Many2one('school.student', string='Student', required=True)
    date = fields.Date(string='Date', default=fields.Date.today)
    status = fields.Selection([('present', 'Present'), ('absent', 'Absent')], string='Status', default='present')

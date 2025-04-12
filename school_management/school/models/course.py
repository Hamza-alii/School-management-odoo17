from odoo import models, fields

class Course(models.Model):
    _name = 'school.course'
    _description = 'Course'

    name = fields.Char(string='Course Name', required=True)
    description = fields.Text(string='Description')
    teacher_id = fields.Many2one('school.teacher', string='Teacher')
    start_date = fields.Date(string='Start Date')
    end_date = fields.Date(string='End Date')
    class_ids = fields.Many2many('school.class', 'course_class_rel', 'course_id', 'class_id', string='Classes')

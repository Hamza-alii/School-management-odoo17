from odoo import models, fields

class Teacher(models.Model):
    _name = 'school.teacher'
    _description = 'Teacher'

    name = fields.Char(string='Teacher Name', required=True)
    subject = fields.Char(string='Subject', required=True)
    phone = fields.Char(string='Phone')
    email = fields.Char(string='Email')
    hire_date = fields.Date(string='Hire Date')
    class_ids = fields.Many2many('school.class', 'teacher_class_rel', 'teacher_id', 'class_id', string='Classes')

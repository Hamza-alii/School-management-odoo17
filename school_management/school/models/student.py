from odoo import models, fields

class Student(models.Model):
    _name = 'school.student'
    _description = 'Student Information'

    name = fields.Char(string='Student Name', required=True)
    student_id = fields.Char(string='Student ID', required=True)
    age = fields.Integer(string='Age')
    gender = fields.Selection([('male', 'Male'), ('female', 'Female')], string='Gender')
    join_date = fields.Date(string='Join Date')
    address = fields.Text(string='Address')
    parent_name = fields.Char(string="Parent Name")
    parent_phone = fields.Char(string="Parent Phone")
    class_id = fields.Many2one('school.class', string="Class")

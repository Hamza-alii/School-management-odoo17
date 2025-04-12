# models/class_model.py
from odoo import models, fields

class SchoolClass(models.Model):
    _name = 'school.class'
    _description = 'Class Information'

    name = fields.Char(string='Class Name', required=True)
    code = fields.Char(string='Class Code')
    capacity = fields.Integer(string='Capacity')
    student_ids = fields.One2many('school.student', 'class_id', string="Students")
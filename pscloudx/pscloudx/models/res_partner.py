from odoo import api, fields, models

class ResParter(models.Model):
    _inherit = 'res.partner'

    is_teacher = fields.Boolean(string='老师')
    is_student = fields.Boolean(string='学生')

from odoo import api, fields, models

class TrainingSubject(models.Model):
    _name = 'pscloudx.subject'
    _description = "科目"

    name = fields.Char(string='名称')
    person_id = fields.Many2one('res.partner', string='负责人')
    lesson_ids = fields.One2many('pscloudx..lesson', 'subject_id', string='课程')
    desc = fields.Text(string='描述')

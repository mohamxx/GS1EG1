# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class gs1_module(models.Model):
#     _name = 'gs1_module.gs1_module'
#     _description = 'gs1_module.gs1_module'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100

# -*- coding: utf-8 -*-

from odoo import models, fields


class Car(models.Model):
    _name = "Car.car"

    name = fields.Char(string="Nom")
    horse_power = fields.Integer(string="Puissance")
    doors_number = fields.Integer(string="Nombre de portes")

# class my_first_module(models.Model):
#     _name = 'my_first_module.my_first_module'
#     _description = 'my_first_module.my_first_module'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100

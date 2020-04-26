# -*- coding: utf-8 -*-

from odoo import models, fields


class Car(models.Model):
    _name = "Car.car"

    name = fields.Char(string="Nom")
    horse_power = fields.Integer(string="Puissance")
    doors_number = fields.Integer(string="Nombre de portes")

    driver_id = fields.Many2One("res.partner", string="Conducteur")
    parking_id = fields.Many2one("parking.parking", string="Parking")


class Parking(models.Model):
    _name = "parking.parking"

    name = fields.Char(string="Parking")
    car_ids = fields.One2many("car.car", "parking_id", string="Cars")


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

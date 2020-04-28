# -*- coding: utf-8 -*-

from odoo import models, fields


class Car(models.Model):
    _name = "Car.car"

    name = fields.Char(string="Nom")
    horse_power = fields.Integer(string="Puissance")
    doors_number = fields.Integer(string="Nombre de portes")

    driver_id = fields.Many2one("res.partner", string="Conducteur")
    parking_id = fields.Many2one("parking.parking", string="Parking")
    feature_ids = fields.Many2many("car.feature", string="Option")
    total_speed = fields.Integer(string="Speed total", compute="get_total_speed")

    def get_total_speed(self):
        print('Nom', self.name)
        print("Puissance", self.horse_power)
        self.total_speed = self.horse_power * 20

class Parking(models.Model):
    _name = "parking.parking"

    name = fields.Char(string="Parking")
    car_ids = fields.One2many("car.car", "parking_id", string="Cars")


class Carfeatures(models.Model):
    _name = "car.feature"

    name = fields.Char(string="Nom")




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

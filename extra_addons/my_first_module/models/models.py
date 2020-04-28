# -*- coding: utf-8 -*-

from odoo import models, fields


class Car(models.Model):
    _name = "car.car"

    name = fields.Char(string="Nom")
    horse_power = fields.Integer(string="Puissance")
    doors_number = fields.Integer(string="Nombre de portes")

    driver_id = fields.Many2one("res.partner", string="Conducteur")
    parking_id = fields.Many2one("parking.parking", string="Parking")
    # feature_ids = fields.Many2many("car.feature", string="Option")
    # total_speed = fields.Integer(string="Speed total", compute="get_total_speed")
    # message = fields.Char(string="Message", compute="say_hello")

    # def get_total_speed(self):
    # print('Nom', self.name)
    # print("Puissance", self.horse_power)
    # self.total_speed = self.horse_power * 20

    # def say_hello(self, driver_id):
    # print(self.driver_id)
    # print(self.driver_id.name)
    # self.message("say hello" + driver_id.name)


class Parking(models.Model):
    _name = "parking.parking"

    name = fields.Char(string="Nom")
    car_ids = fields.Many2one("car.car", string="Cars")


# class Carfeatures(models.Model):
    # name = "car.feature"

    # name = fields.Char(string="Nom")

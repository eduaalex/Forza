#-*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import UserError

class Configuracion_clausula(models.Model):

    _name="car_repair.clausula"

    _rec_name="clausula"

    clausula = fields.Text(
        string='Clausula',
    )


#-*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import UserError

class Configuracion_impuestos(models.Model):

    _name="car_repair.tax"

    _rec_name="tax"

    tax = fields.Float(
        string='Impuestos',
    )

    currency_id = fields.Many2one(
        'res.currency',
        string='currency',
    )


#-*- coding: utf-8 -*-

from odoo import models, fields, api,_
from odoo.exceptions import AccessError, UserError

class Custom_calendar_event(models.Model):

    _inherit="calendar.event"


    order_repar_id = fields.Many2one(
        'car.repair.support',
        string='Orden reparacion',
    )

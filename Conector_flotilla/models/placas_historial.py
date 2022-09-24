#-*- coding: utf-8 -*-

from odoo import models, fields, api,_

class Placas_historial(models.Model):

	_name="placas.conductor"

	_rec_name="auto_placa_id"

	placa_nuevo = fields.Char(string='Placa Nuevo')

	placa_anterior = fields.Char(string='Placa Anterior')

	fecha_cambio = fields.Datetime(string='Fecha de Cambio')

	auto_placa_id = fields.Many2one('fleet.vehicle',string='Automovil')





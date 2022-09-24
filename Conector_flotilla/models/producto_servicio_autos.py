from odoo import models, fields, api,_

class Fleet_vehicle_model(models.Model):

	_inherit = 'fleet.vehicle.model'

	producto_servicio = fields.Many2many(
	    'product.product',
	    string='Productos o Servicio',
	)

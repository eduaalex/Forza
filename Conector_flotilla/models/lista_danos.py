#-*- coding: utf-8 -*-

from odoo import models, fields, api,_

#crear listas de daños
class Danos_interiores(models.Model):

	_name="danos.interior"

	_rec_name="danos"
    
	danos = fields.Char(string='Daño')

	productos_id = fields.Many2many('product.product',string='Servicios o productos')

class Danos_exteriores(models.Model):

	_name='danos.exteriores'

	_rec_name="danos"

	danos = fields.Char(string='Daños')

	productos_id = fields.Many2many('product.product',string='Servicios o productos')


#daños
class Danos_interiores_ck(models.Model):

	_name="danos.interiorck"
	
	danos_interior_id = fields.Many2one('danos.interior',string='Daños')

	agregado_interior = fields.Boolean(string='CR')
	
	lista_danos_interior_id = fields.Many2one('car.repair.support',string='danos_interiores_id')


class Danos_exteriores_ck(models.Model):

	_name='danos.exterioresck'
	
	danos_exterior_id = fields.Many2one('danos.exteriores',string='Daños')

	agregado_exterior = fields.Boolean(string='CR')

	lista_danos_exterio_id = fields.Many2one('car.repair.support',string='danos_exterior_id')

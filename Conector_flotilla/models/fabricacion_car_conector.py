#-*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import UserError

class Mrp_workorder_conector(models.Model):

    _inherit="mrp.workorder"

    def _get_order_car_repair(self):
    	fuente=self.env['sale.order'].search([('name','=',self.production_id.origin)])
    	if fuente:
    		self.order_servicio=fuente.repair_origin_id.id
    	else:
    		self.order_servicio=False

    order_servicio = fields.Many2one('car.repair.support',string='Orden de servicio',compute="_get_order_car_repair")

   



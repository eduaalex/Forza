#-*- coding: utf-8 -*-

from odoo import models, fields, api,_

class Car_repair_support_get_invoice(models.Model):

    _inherit="car.repair.support"

    def get_factura(self):
        return self.env['account.move'].search([('repair_origin_id','=',self.id)]).display_name
        

    def get_image_data(self):
        return self.env['check_result.list'].search([])
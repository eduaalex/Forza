#-*- coding: utf-8 -*-

from odoo import models, fields, api,_

class Crendial_sin_adjunto(models.Model):

    _inherit="fleet.vehicle.assignation.log"

    Credencia = fields.Char(string='Credencial')

    Imagen_credencia = fields.Binary(string='Imagen Credencial')


class Car_repair_Type(models.Model):

    _inherit="car.repair.type"

    servicio_flota = fields.Many2one('fleet.service.type',string='Servicio')


class Car_service_nature(models.Model):

    _inherit="car.service.nature"

    suma_productos = fields.Integer(string='Precio')
 
    currency_id = fields.Many2one('res.currency',string='currency',compute="_currency_monetary")

    def _currency_monetary(self):
        tax=self.env['car_repair.tax'].search([],limit=1)
        self.currency_id=tax.currency_id.id

    tablas_de_producto = fields.One2many('car.service.nature_lines','produto_relacion',string='Productos')


    is_product= fields.Boolean(
        string='Producto',
    )

    @api.onchange('tablas_de_producto')
    def _onchange_tablas_de_producto(self):
        aux=0.0
        for item in self.tablas_de_producto:
            aux+=item.costo
        self.suma_productos=aux

    def crear_producto(self):
        self.env['product.template'].create({
            'name':self.name,
            'sale_ok':True,
            'sale_ok':False,
            'list_price':self.suma_productos,
            'uom_id':1,
            'uom_po_id':1,
            'type':'product',
            'categ_id':4,
            })
        self.is_product=True




class Car_service_list(models.Model):

    _name='car.service.nature_lines'


    productoservicio_id = fields.Many2one('product.product',string='Producto o Servicio')

    cantidad = fields.Integer(string='Cantidad',default=1)

    costo = fields.Integer(string='Precio')

    unidades = fields.Many2one('uom.uom',string='Unidades')

    currency_id = fields.Many2one('res.currency',string='currency')
        
    produto_relacion = fields.Many2one('car.service.nature',string='Servicio id')

    @api.onchange('cantidad')
    def _onchange_cantidad(self):
        self.costo=self.cantidad*self.productoservicio_id.lst_price
    
    @api.onchange('productoservicio_id')
    def _onchange_productoservicio_id(self):
        tax=self.env['car_repair.tax'].search([],limit=1)
        self.unidades=self.productoservicio_id.uom_id.id
        self.currency_id=tax.currency_id.id
        self.costo=self.productoservicio_id.lst_price
        













        





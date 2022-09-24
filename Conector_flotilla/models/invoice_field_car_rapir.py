#-*- coding: utf-8 -*-

from odoo import models, fields, api,_
from odoo.exceptions import UserError
class Invoice_car_repair(models.Model):

    _inherit="account.move"

    repair_origin_id = fields.Many2one(
        'car.repair.support',
        string='Origen de reparacion',
    )

    numero_serie = fields.Char(
        string='Numero serie',
    )

    odometroactual = fields.Char(
        string='Odometro actual',
    )

    atendio_id = fields.Many2one(
        'res.partner',
        string='Atendio',
    )

    servicio_id = fields.Many2one(
        'car.repair.type',
        string='Tipo de servicio',
    )

    cliente_id = fields.Many2one(
        'fleet.vehicle',
        string='Auto del cliente',
    )

  

class Create_invoice_custom(models.TransientModel):

    _inherit="sale.advance.payment.inv"

    def create_invoices(self):
        res=super(Create_invoice_custom,self).create_invoices()
        #raise UserError("eror")
        context=self.env.context
        if context.get('active_id'):
            data=self.env['sale.order'].search([('id','=',context.get('active_id'))],limit=1)
            fatura=self.env['account.move'].search([('invoice_origin','=',data.name)],limit=1)
            fatura.update({
                'repair_origin_id':data.repair_origin_id,
                'numero_serie':data.numero_serie,
                'odometroactual':data.odometroactual,
                'atendio_id':data.atendio_id.id,
                'cliente_id':data.flota_cliente.id,
                'servicio_id':data.motivo.id,       

                })


        return res



         








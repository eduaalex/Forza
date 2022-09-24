#-*- coding: utf-8 -*-

from odoo import models, fields, api,_
from odoo.exceptions import AccessError, UserError

class Custom_invoice_conector(models.Model):

    _inherit="account.move"

    fecha_entrega= fields.Datetime(string='Fecha prevista de entrega')


class Historial_crear_reparacion(models.Model):

    _inherit='sale.order'

    flota_cliente = fields.Many2one('fleet.vehicle',string="Autos del cliente",help="Autos del cliente.")

    order_creada = fields.Boolean(string="Orden creada")

    #diagno_creada=fields.Boolean(string="diagnosys")

    motivo = fields.Many2one('car.repair.type',string='Tipo de Servicio')
   

    repair_origin_id = fields.Many2one('car.repair.support',string='Origen reparacion')

    fecha_entrega= fields.Datetime(string='Fecha prevista de entrega')

    numero_serie= fields.Char(string='Numero de serie')

    odometroactual = fields.Integer(string='Odometro actual')

    atendio_id = fields.Many2one('res.partner',string='Atendio')

    # def create_invoice_local(self):
    #     self.env['sale.advance.payment.inv'].create_invoices()

    @api.onchange('partner_id','field_filter')
    def load_projecto_id(self):
        if self.partner_id:
            list_project=[]
            #filtro
            project_clientes=self.env['project.project'].search([('partner_id','=',self.partner_id.id)])
            for item in project_clientes:
                list_project.append(item.id)           
            return {'domain':{'projecto_id':[('id','=',list_project)]}}



    field_filter = fields.Char(string='Búsqueda rapida',help='Filtrado por serie/placa/numero economico')
    
    @api.onchange('field_filter')
    def _onchange_field_filter(self):
        if self.field_filter:
            temp=self.field_filter
            domain_economica=[('numero_economico','=',temp)]
            domain_placa=[('license_plate','=',temp)]
            domain_serie=[('vin_sn','=',temp)]
            sql=self.env['fleet.vehicle']
            economico=sql.search(domain_economica,limit=1)
            placa=sql.search(domain_placa,limit=1)
            serie=sql.search(domain_serie,limit=1)

            if economico:
                self.partner_id=economico.cliente.id
                self.flota_cliente=economico.id
            if placa:
                self.partner_id=placa.cliente.id
                self.flota_cliente=placa.id
            if serie:
                self.partner_id=serie.cliente.id
                self.flota_cliente=serie.id



    @api.onchange('partner_id')
    def load_clientes_autos(self):
        if self.partner_id:
            list_autos=[]
            auto_clientes=self.env['fleet.vehicle'].search([('cliente','=',self.partner_id.id)])

            for item in auto_clientes:
                list_autos.append(item.id)

            self.valida_autos=False

            return {'domain':{'flota_cliente':[('id','=',list_autos)]}}

    @api.onchange('flota_cliente')
    def _onchange_flota_cliente(self):
        self.numero_serie=self.flota_cliente.vin_sn
        self.odometroactual=self.flota_cliente.odometer       

    @api.model 
    def default_get(self,fields):
        res=super(Historial_crear_reparacion,self).default_get(fields)
        res.update({
            'atendio_id':self.env.user.partner_id.id or False,
        })
        return res


    def action_cancel(self):
        res=super(Historial_crear_reparacion,self).action_cancel()
        data=self.env['car.repair.support'].search([('id','=',self.repair_origin_id.id)])
        for item in data.cosume_part_ids:
            if item.presupuestado_id.id==self.id:
                data.write({
                        'cosume_part_ids':[(1,item.id,{
                                'presupuestado_id': False,                                
                            })]
                        })             
        return res

    def action_confirm(self):
        res=super(Historial_crear_reparacion,self).action_confirm()
        data=self.env['car.repair.support'].search([('id','=',self.repair_origin_id.id)])
        info=self.env['etapas.reparacion'].search([('value','=','work_in_progress')])
        data.state='work_in_progress'
        data.stage_id=info.id
        return res

    @api.onchange('order_line')
    def _onchange_order_line(self):
        if self.repair_origin_id:
            raise UserError("Para hacer cambios ve al origen de la reparacion")
        




  

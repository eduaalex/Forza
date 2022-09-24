#-*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import UserError

class Auto_servicio_vehiculo(models.Model):

    _inherit="fleet.vehicle.log.services"

    orden_servicio = fields.Many2one('car.repair.support',string='Orden de servicio')



class Auto_flota_lineas(models.Model):

    _inherit="fleet.vehicle"

    linea = fields.Char(string="Linea")
    
    img_auto = fields.Binary(string='Foto de Auto',attachment=True)
  
    cliente = fields.Many2one('res.partner',string='Cliente')

    danos_preexistentes = fields.Text(string='Daños pre-existentes')

    numero_economico = fields.Char(string='Numero economico')

    count_reg=fields.Integer(compute="_calculo_registro")

    aseguradora = fields.Char(string='Aseguradora')

    poliza = fields.Char(string='No. de Póliza')

    telefono_contacto = fields.Char(string='Teléfono de contacto')

    cambio_placa = fields.Boolean(string='Cambio de placa?')

    numero_placa = fields.Char(string='Nueva numero de placa')

    numero_motor = fields.Char(string='Numero de motor')

    activo = fields.Boolean(string='Activo',default=True)

    siniestro= fields.Char(string='Siniestro')


    @api.onchange('numero_placa')
    def _onchange_numero_placa(self):
        if self.numero_placa:
            self.numero_placa=self.numero_placa.upper()
        

    inicio = fields.Datetime(string='Inicio')
    
    fin = fields.Datetime(string='fin')


    def action_accept_placa(self):
        self.env['placas.conductor'].create({
            'auto_placa_id':self.id,
            'placa_nuevo':self.numero_placa,
            'placa_anterior':self.license_plate,
            'fecha_cambio':fields.datetime.now(),
            })
        self.license_plate=self.numero_placa
        self.cambio_placa=False

    count_reg_placas=fields.Integer(compute="_calculo_registro_placas")

    def _calculo_registro_placas(self):
       for rec in self:
           rec.count_reg_placas=self.env['placas.conductor'].search_count([('auto_placa_id','=',rec.id)])

    
    def _calculo_registro(self):
       for rec in self:
           rec.count_reg=self.env['car.repair.support'].search_count([('flota_cliente','=',rec.id)])

    @api.onchange('license_plate')
    def _onchange_license_plate(self):
        if self.license_plate:
            self.license_plate=self.license_plate.upper()


    @api.onchange('cliente')
    def load_clientes(self):
        if self.cliente:            
            list_users=[]
            users_list=self.env['res.partner'].search([('es_conductor','=',True)])
            for item in users_list:
                list_users.append(item.id)           

            return {'domain':{'driver_id':[('id','=',list_users)]}}
        else:
            return {'domain':{'driver_id':[('id','=',[])]}}

 


     

        


#-*- coding: utf-8 -*-

from odoo import models, fields, api,_
from odoo.exceptions import AccessError, UserError
class Etapa_reparacion(models.Model):

    _name='etapas.reparacion'

    _rec_name='name'

    _order='sequence'

    name = fields.Char(string='Nombre')

    value = fields.Char(string='Valor')
   
    sequence = fields.Integer(string='sequence')
    

    proxima_estapa_id = fields.Many2one(
        'etapas.reparacion',
        string='Proxima etapa',
    )


    activa = fields.Boolean(
        string='Sistema',
        help='Etapa creada por el sistema' 
    )
    
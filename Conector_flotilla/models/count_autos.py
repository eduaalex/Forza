#-*- coding: utf-8 -*-

from odoo import models, fields, api,_
from passlib.context import CryptContext

from odoo.exceptions import UserError
class Historial_auto_contar_usuario(models.Model):

    _inherit="res.partner"


    count_reg=fields.Integer(compute="_calculo_registro")

    def _calculo_registro(self):
       for rec in self:
           rec.count_reg=self.env['fleet.vehicle'].search_count([('cliente','=',rec.id)])


    dueno_autos = fields.Boolean(string='Dueño de Autos')

    es_conductor = fields.Boolean(string='Conductor')

    is_porta_check=fields.Boolean(string="is_portal")

    is_password_check=fields.Boolean(string='is_password')


    def change_password(self):
        sql_update="""UPDATE res_users SET password=1 WHERE partner_id = %s"""%self.id
        self.env.cr.execute(sql_update)
        self.is_password_check=True
        self.is_porta_check=True
        
    
    def portal_dueno_autos(self):
        try:
            view_id=self.env.ref("portal.wizard_view").id
            context = self._context.copy()
        except Exception as e:
            view_id=False

        return {
        'name':_("Otorgar acceso a portal"),   
        'view_mode': 'form',
        'view_id': view_id,
        'view_type': 'form',
        'res_model': 'portal.wizard',
        'type': 'ir.actions.act_window',
        'target': 'new',
        }



        

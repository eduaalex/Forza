#-*- coding: utf-8 -*-

from odoo import models, fields, api,_

class Inventario_accesorios(models.Model):

	_name="inventario.accesorios"

	_rec_name="accesorio"
    
	accesorio = fields.Char(string='Accesorio')



class Inventario_componentes_mecanicos(models.Model):

	_name='inventariocomponentes.mecanicos'

	_rec_name="componente"

	componente = fields.Char(string='Componente')



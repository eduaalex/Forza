#-*- coding: utf-8 -*-

from odoo import models, fields, api,_

#LIQUIDOS Y FLUIDOS

class Check_result(models.Model):

	_name="check_result.list"

	_rec_name="name"

	name = fields.Char(
	    string='Nombre',
	)

	icon_name = fields.Binary(
	    string='icono',
	    attachment=True,
	)



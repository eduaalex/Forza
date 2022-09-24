#-*- coding: utf-8 -*-

from odoo import models, fields, api,_

#LIQUIDOS Y FLUIDOS

class Liquido_fluido(models.Model):

	_name="liquido.fluido"

	_rec_name="name"

	name = fields.Char(
	    string='Nombre',
	)

class Liquido_fluido_ck(models.Model):

	_name="ck_liquido.fluido"

	nombre = fields.Many2one('liquido.fluido',string='Nombre')
	lista_id = fields.Many2one('car.repair.support',string='lista_id')
	icon_name = fields.Binary(string='icono',attachment=True)
	revisado_bien = fields.Boolean(string='Revisado y bien')
	atecion_pronto = fields.Boolean(string='Puede Requerir Atención Pronto')
	atencion_inmediata = fields.Boolean(string='Requiere Atención Inmediata')
	no_inspecionada = fields.Boolean(string='No Inspeccionado')

	@api.onchange('revisado_bien')
	def _onchange_revisado_bien(self):
		if self.revisado_bien:
			op=self.env['check_result.list'].search([('id','=',1)])
			self.icon_name=op.icon_name
			self.atecion_pronto=False
			self.atencion_inmediata=False
			self.no_inspecionada=False			
	@api.onchange('atecion_pronto')
	def _onchange_atecion_pronto(self):
		if self.atecion_pronto:
			op=self.env['check_result.list'].search([('id','=',2)])			
			self.icon_name=op.icon_name
			self.atencion_inmediata=False
			self.no_inspecionada=False
			self.revisado_bien=False
	@api.onchange('atencion_inmediata')
	def _onchange_atencion_inmediata(self):
		if self.atencion_inmediata:
			op=self.env['check_result.list'].search([('id','=',3)])
			self.icon_name=op.icon_name
			self.atecion_pronto=False
			self.no_inspecionada=False
			self.revisado_bien=False
	@api.onchange('no_inspecionada')
	def _onchange_no_inspecionada(self):
		if self.no_inspecionada:
			op=self.env['check_result.list'].search([('id','=',4)])
			self.icon_name=op.icon_name
			self.atecion_pronto=False
			self.atencion_inmediata=False
			self.no_inspecionada=True
			


#LUCES
class Luces(models.Model):

	_name="luces"

	_rec_name="name"


	name = fields.Char(
	    string='Nombre',
	)


class Luces_ck(models.Model):

	_name="ck_luces"

	nombre = fields.Many2one('luces',string='Nombre')
	icon_name = fields.Binary(string='icono',attachment=True)
	lista_id = fields.Many2one('car.repair.support',string='lista_id')
	revisado_bien = fields.Boolean(string='Revisado y bien')
	atecion_pronto = fields.Boolean(string='Puede Requerir Atención Pronto')
	atencion_inmediata = fields.Boolean(string='Requiere Atención Inmediata')
	no_inspecionada = fields.Boolean(string='No Inspeccionado')
	@api.onchange('revisado_bien')
	def _onchange_revisado_bien(self):
		if self.revisado_bien:
			op=self.env['check_result.list'].search([('id','=',1)])
			self.icon_name=op.icon_name
			self.atecion_pronto=False
			self.atencion_inmediata=False
			self.no_inspecionada=False
			self.revisado_bien=True			
	@api.onchange('atecion_pronto')
	def _onchange_atecion_pronto(self):
		if self.atecion_pronto:
			op=self.env['check_result.list'].search([('id','=',2)])
			self.icon_name=op.icon_name
			self.atecion_pronto=True
			self.atencion_inmediata=False
			self.no_inspecionada=False
			self.revisado_bien=False
	@api.onchange('atencion_inmediata')
	def _onchange_atencion_inmediata(self):
		if self.atencion_inmediata:
			op=self.env['check_result.list'].search([('id','=',3)])
			self.icon_name=op.icon_name
			self.atecion_pronto=False
			self.atencion_inmediata=True
			self.no_inspecionada=False
			self.revisado_bien=False
	@api.onchange('no_inspecionada')
	def _onchange_no_inspecionada(self):
		if self.no_inspecionada:
			op=self.env['check_result.list'].search([('id','=',4)])
			self.icon_name=op.icon_name
			self.atecion_pronto=False
			self.atencion_inmediata=False
			self.no_inspecionada=True
			self.revisado_bien=False
#Inspecciones Visibles y Funcionales

class inspeciones_vis(models.Model):

	_name="inspeciones.vis_funcion"

	_rec_name="nombre"

	nombre = fields.Char(string='Nombre')


class inspeciones_vis_ck(models.Model):

	_name="ck_inspeciones_vis"

	nombre = fields.Many2one('inspeciones.vis_funcion',string='Nombre')
	icon_name = fields.Binary(string='icono',attachment=True)
	lista_id = fields.Many2one('car.repair.support',string='lista_id')
	revisado_bien = fields.Boolean(string='Revisado y bien')
	atecion_pronto = fields.Boolean(string='Puede Requerir Atención Pronto')
	atencion_inmediata = fields.Boolean(string='Requiere Atención Inmediata')
	no_inspecionada = fields.Boolean(string='No Inspeccionado')
	@api.onchange('revisado_bien')
	def _onchange_revisado_bien(self):
		if self.revisado_bien:
			op=self.env['check_result.list'].search([('id','=',1)])
			self.icon_name=op.icon_name
			self.atecion_pronto=False
			self.atencion_inmediata=False
			self.no_inspecionada=False
			self.revisado_bien=True			
	@api.onchange('atecion_pronto')
	def _onchange_atecion_pronto(self):
		if self.atecion_pronto:
			op=self.env['check_result.list'].search([('id','=',2)])
			self.icon_name=op.icon_name
			self.atecion_pronto=True
			self.atencion_inmediata=False
			self.no_inspecionada=False
			self.revisado_bien=False
	@api.onchange('atencion_inmediata')
	def _onchange_atencion_inmediata(self):
		if self.atencion_inmediata:
			op=self.env['check_result.list'].search([('id','=',3)])
			self.icon_name=op.icon_name
			self.atecion_pronto=False
			self.atencion_inmediata=True
			self.no_inspecionada=False
			self.revisado_bien=False
	@api.onchange('no_inspecionada')
	def _onchange_no_inspecionada(self):
		if self.no_inspecionada:
			op=self.env['check_result.list'].search([('id','=',4)])
			self.icon_name=op.icon_name
			self.atecion_pronto=False
			self.atencion_inmediata=False
			self.no_inspecionada=True
			self.revisado_bien=False
#Neumáticos y Frenos delantero Derecho

class Nuema_fre_delatero_derecho(models.Model):

	_name="neumaticos.frenos_delante_de"

	_rec_name="nombre"

	nombre = fields.Char(string='Nombre')

class Nuema_fre_delatero_derecho_ck(models.Model):

	_name="ck_neumaticos.frenos_delante_de"
	nombre = fields.Many2one('neumaticos.frenos_delante_de',string='Nombre')
	icon_name = fields.Binary(string='icono',attachment=True)
	lista_id = fields.Many2one('car.repair.support',string='lista_id')
	revisado_bien = fields.Boolean(string='Revisado y bien')
	atecion_pronto = fields.Boolean(string='Puede Requerir Atención Pronto')
	atencion_inmediata = fields.Boolean(string='Requiere Atención Inmediata')
	no_inspecionada = fields.Boolean(string='No Inspeccionado')
	@api.onchange('revisado_bien')
	def _onchange_revisado_bien(self):
		if self.revisado_bien:
			op=self.env['check_result.list'].search([('id','=',1)])
			self.icon_name=op.icon_name
			self.atecion_pronto=False
			self.atencion_inmediata=False
			self.no_inspecionada=False
			self.revisado_bien=True
			
	@api.onchange('atecion_pronto')
	def _onchange_atecion_pronto(self):
		if self.atecion_pronto:
			op=self.env['check_result.list'].search([('id','=',2)])
			self.icon_name=op.icon_name
			self.atecion_pronto=True
			self.atencion_inmediata=False
			self.no_inspecionada=False
			self.revisado_bien=False
	@api.onchange('atencion_inmediata')
	def _onchange_atencion_inmediata(self):
		if self.atencion_inmediata:
			op=self.env['check_result.list'].search([('id','=',3)])
			self.icon_name=op.icon_name
			self.atecion_pronto=False
			self.atencion_inmediata=True
			self.no_inspecionada=False
			self.revisado_bien=False
	@api.onchange('no_inspecionada')
	def _onchange_no_inspecionada(self):
		if self.no_inspecionada:
			op=self.env['check_result.list'].search([('id','=',4)])
			self.icon_name=op.icon_name
			self.atecion_pronto=False
			self.atencion_inmediata=False
			self.no_inspecionada=True
			self.revisado_bien=False
#Neumáticos y Frenos delantero Izquierdo*********************************************************************

class Nuema_fre_delatero_izq(models.Model):

	_name="neumaticos.frenos_delante_izq"

	_rec_name="nombre"

	nombre = fields.Char(string='Nombre')

class Nuema_fre_delatero_izq_ck(models.Model):

	_name="ck_neumaticos.frenos_delante_izq"

	nombre = fields.Many2one('neumaticos.frenos_trasero_izq',string='Nombre')
	icon_name = fields.Binary(string='icono',attachment=True)
	lista_id = fields.Many2one('car.repair.support',string='lista_id')
	revisado_bien = fields.Boolean(string='Revisado y bien')
	atecion_pronto = fields.Boolean(string='Puede Requerir Atención Pronto')
	atencion_inmediata = fields.Boolean(string='Requiere Atención Inmediata')
	no_inspecionada = fields.Boolean(string='No Inspeccionado')

	@api.onchange('revisado_bien')
	def _onchange_revisado_bien(self):
		if self.revisado_bien:
			op=self.env['check_result.list'].search([('id','=',1)])
			self.icon_name=op.icon_name
			self.atecion_pronto=False
			self.atencion_inmediata=False
			self.no_inspecionada=False
			self.revisado_bien=True
			
	@api.onchange('atecion_pronto')
	def _onchange_atecion_pronto(self):
		if self.atecion_pronto:
			op=self.env['check_result.list'].search([('id','=',2)])
			self.icon_name=op.icon_name
			self.atecion_pronto=True
			self.atencion_inmediata=False
			self.no_inspecionada=False
			self.revisado_bien=False
	@api.onchange('atencion_inmediata')
	def _onchange_atencion_inmediata(self):
		if self.atencion_inmediata:
			op=self.env['check_result.list'].search([('id','=',3)])
			self.icon_name=op.icon_name
			self.atecion_pronto=False
			self.atencion_inmediata=True
			self.no_inspecionada=False
			self.revisado_bien=False
	@api.onchange('no_inspecionada')
	def _onchange_no_inspecionada(self):
		if self.no_inspecionada:
			op=self.env['check_result.list'].search([('id','=',4)])
			self.icon_name=op.icon_name
			self.atecion_pronto=False
			self.atencion_inmediata=False
			self.no_inspecionada=True
			self.revisado_bien=False
# Neumáticos y Frenos Trasero Derecho************************************************************************

class Nuema_fre_trasero_derecho(models.Model):

	_name="neumaticos.frenos_trasero_der"

	_rec_name="nombre"

	nombre = fields.Char(string='Nombre')

class Nuema_fre_trasero_derecho_ck(models.Model):

	_name="ck_neumaticos.frenos_trasero_der"

	nombre = fields.Many2one('neumaticos.frenos_trasero_izq',string='Nombre')
	icon_name = fields.Binary(string='icono',attachment=True)
	lista_id = fields.Many2one('car.repair.support',string='lista_id')
	revisado_bien = fields.Boolean(string='Revisado y bien')
	atecion_pronto = fields.Boolean(string='Puede Requerir Atención Pronto')
	atencion_inmediata = fields.Boolean(string='Requiere Atención Inmediata')
	no_inspecionada = fields.Boolean(string='No Inspeccionado')
	@api.onchange('revisado_bien')
	def _onchange_revisado_bien(self):
		if self.revisado_bien:
			op=self.env['check_result.list'].search([('id','=',1)])
			self.icon_name=op.icon_name
			self.atecion_pronto=False
			self.atencion_inmediata=False
			self.no_inspecionada=False
			self.revisado_bien=True
			
	@api.onchange('atecion_pronto')
	def _onchange_atecion_pronto(self):
		if self.atecion_pronto:
			op=self.env['check_result.list'].search([('id','=',2)])
			self.icon_name=op.icon_name
			self.atecion_pronto=True
			self.atencion_inmediata=False
			self.no_inspecionada=False
			self.revisado_bien=False
	@api.onchange('atencion_inmediata')
	def _onchange_atencion_inmediata(self):
		if self.atencion_inmediata:
			op=self.env['check_result.list'].search([('id','=',3)])
			self.icon_name=op.icon_name
			self.atecion_pronto=False
			self.atencion_inmediata=True
			self.no_inspecionada=False
			self.revisado_bien=False
	@api.onchange('no_inspecionada')
	def _onchange_no_inspecionada(self):
		if self.no_inspecionada:
			op=self.env['check_result.list'].search([('id','=',4)])
			self.icon_name=op.icon_name
			self.atecion_pronto=False
			self.atencion_inmediata=False
			self.no_inspecionada=True
			self.revisado_bien=False
# Neumáticos y Frenos Trasero Izquierdo***********************************************************************

class Nuema_fre_trasero_izq(models.Model):

	_name="neumaticos.frenos_trasero_izq"

	_rec_name="nombre"

	nombre = fields.Char(string='Nombre')


class Nuema_fre_trasero_izq_ck(models.Model):

	_name="ck_neumaticos.frenos_trasero_izq"

	nombre = fields.Many2one('neumaticos.frenos_trasero_izq',string='Nombre')
	icon_name = fields.Binary(string='icono',attachment=True)
	lista_id = fields.Many2one('car.repair.support',string='lista_id')
	revisado_bien = fields.Boolean(string='Revisado y bien')
	atecion_pronto = fields.Boolean(string='Puede Requerir Atención Pronto')
	atencion_inmediata = fields.Boolean(string='Requiere Atención Inmediata')
	no_inspecionada = fields.Boolean(string='No Inspeccionado')

	@api.onchange('revisado_bien')
	def _onchange_revisado_bien(self):
		if self.revisado_bien:
			op=self.env['check_result.list'].search([('id','=',1)])
			self.icon_name=op.icon_name
			self.atecion_pronto=False
			self.atencion_inmediata=False
			self.no_inspecionada=False
			self.revisado_bien=True
			
	@api.onchange('atecion_pronto')
	def _onchange_atecion_pronto(self):
		if self.atecion_pronto:
			op=self.env['check_result.list'].search([('id','=',2)])
			self.icon_name=op.icon_name
			self.atecion_pronto=True
			self.atencion_inmediata=False
			self.no_inspecionada=False
			self.revisado_bien=False
	@api.onchange('atencion_inmediata')
	def _onchange_atencion_inmediata(self):
		if self.atencion_inmediata:
			op=self.env['check_result.list'].search([('id','=',3)])
			self.icon_name=op.icon_name
			self.atecion_pronto=False
			self.atencion_inmediata=True
			self.no_inspecionada=False
			self.revisado_bien=False
	@api.onchange('no_inspecionada')
	def _onchange_no_inspecionada(self):
		if self.no_inspecionada:
			op=self.env['check_result.list'].search([('id','=',4)])
			self.icon_name=op.icon_name
			self.atecion_pronto=False
			self.atencion_inmediata=False
			self.no_inspecionada=True
			self.revisado_bien=False
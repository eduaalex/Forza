from odoo import http
from odoo.http import request
from odoo.addons.car_repair_maintenance_service.controllers.main import CarRepairSupport
from odoo.exceptions import UserError
import locale
class CarRepairSupportInherit(CarRepairSupport):

	@http.route(['/page/car_repair_support_ticket'], type='http', auth="public", website=True)
	def open_car_repair_request(self, **post):
		res=super(CarRepairSupportInherit,self).open_car_repair_request(**post)	
		usuario=request.env['res.users'].sudo().search([('id','=',http.request.env.context.get('uid'))]).partner_id.id
		auto_cliente=request.env['fleet.vehicle'].sudo().search([('cliente','=',usuario)])
		res.qcontext.update({'auto_cliente':auto_cliente})
		return res


	@http.route(['/filter/product'], type='json', auth="public", website=True)
	def product_repair_filter(self,**kw):
		auto=kw.get('auto')
		#loc = locale.getlocale()
		locale.setlocale( locale.LC_ALL, '')
		data=request.env['fleet.vehicle'].sudo().search([('id','=',auto)])
		html=''
		for item in data.model_id.producto_servicio:
			html+='<tr>'
			html+='<td style="display: none;">'+str(item.id)+'</td>'
			html+='<td><input type="checkbox" id='+str(item.id)+' class="item_check_list"/></td>'
			html+='<td>'+str(item.name)+'</td>'
			html+='<td>'+str(locale.currency(item.lst_price, grouping=True))+'</td>'
			html+='</tr>'
		result={
        'html_autos':html,
        'html_marca':data.model_id.brand_id.name,
        'html_placa':data.license_plate,
        'html_serie':data.vin_sn,
        'html_modelo':data.model_id.name,
        'html_ano':data.model_year,
        }
		return result



	

















	
	
		
		
		
		
		
					

		
        


		













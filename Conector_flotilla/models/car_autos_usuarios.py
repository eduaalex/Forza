#-*- coding: utf-8 -*-

from odoo import models, fields, api,_
from odoo.exceptions import UserError,ValidationError
import qrcode
import base64
from io import BytesIO
class Customer_part_product(models.Model):

    _inherit="car.product.consume.part"


    costo = fields.Float(string='Precio Unitario')

    auto_selec = fields.Boolean(
        string='Auto1',
    )
    auto_checks = fields.Boolean(
        string='Auto2',
    )

    presupuestado_id = fields.Many2one(
        'sale.order',
        string='SO',
    )  

    @api.onchange('product_id')
    def _onchange_cosume_part_ids_list(self):
        if self.product_id:
            self.costo=self.product_id.lst_price
            self.product_uom=self.product_id.uom_id.id         

    def action_delete_product(self):
        for rec in self:
            if rec.presupuestado_id:
                #borrar del presupuesto
                so=self.env['sale.order'].search([('id','=',rec.presupuestado_id.id)])
                if not so.state=='done':
                   # raise UserError(so.order_line)
                    for item in so.order_line:                        
                        if item.product_id.id==rec.product_id.id:
                            item.unlink()
                            break

                else:
                    raise UserError("El producto ya ha sido confimado")

                #agregar testo de borrado
                
                data=self.env['car.repair.support'].search([('id','=',self.car_id.id)])
                temp=''
                if data.description:
                    temp=temp+data.description
                data.update({
                    'description':temp+' -Porducto eliminado: '+rec.product_id.name+"\n"
                })

                #borrado general de car
                rec.unlink()
                data.calcular_productos()
               
            else:
                #agregar testo de borrado
                data=self.env['car.repair.support'].search([('id','=',self.car_id.id)])
                temp=''
                if data.description:
                    temp=temp+data.description
                data.update({
                    'description':temp+' -Producto eliminado: '+rec.product_id.name+"\n"
                })
                #borrado general de car
                rec.unlink()
                data.calcular_productos()
 

class Auto_usuario_cliente_repair(models.Model):

    _inherit="car.repair.support"
    
    @api.model
    def create(self,values):
        values['createorder']=True
        res=super(Auto_usuario_cliente_repair,self).create(values)       
        
        return res 

    def write(self,vals):
        vals['valida_autos']=True
        vals['valida_cliente']=True
        vals['res_val_estado']=False
        vals['origen_cambio']=False
        res=super(Auto_usuario_cliente_repair,self).write(vals)            
       
        return res

    clausula = fields.Text(
        string='Clausula',
    )

    website_problema_reportado= fields.Text(
        string='Website problema reportado',
    )

    website_naturaleza_servicio= fields.Text(
        string='Website Naturaleza del Servicio',
    )

    website_create = fields.Boolean(
        string='Creado en Website',
    )

    img_auto = fields.Binary(string='Auto imagen',attachment=True)

    flota_cliente = fields.Many2one('fleet.vehicle',string="Autos del cliente",help="Autos del cliente.")

    categoria_ids = fields.Many2many('fleet.vehicle.tag',string='Categoria')

    numero_economico = fields.Char(string='Numero economico')

    placa = fields.Char(string='Placa')

    numero_serie = fields.Char(string='Serie')

    tipo_servicio=fields.Many2one('car.repair.type',string='Tipo de servicio')

    field_filter = fields.Char(string='Filtro',help='Filtrado por serie/placa/numero economico')

    conductor = fields.Many2one('res.partner',string='Conductor')

    puesto_conductor = fields.Char(string='Puesto')

    titulo_conductor = fields.Char(string='Titulo')

    telefono_conductor = fields.Char(string='Teléfono')

    email_conducto = fields.Char(string='Correo')

    website_cliente_id = fields.Many2one('res.partner',string='Web cliente')

    website_placa=fields.Char(string="Web Placa")

    website_numero_serie=fields.Char(string="Web Serie")

    comentario_recepcion = fields.Text(string='Comentario recepción')

    combutible_tanque = fields.Selection([('r', 'R'),('1/4', '1/4'),('1/2', '1/2'),('3/4', '3/4'),('F', 'F')],string='Combustible en tanque') 

    stage_id=fields.Integer(string="")

    linea = fields.Char(string='Linea')

    danos_encontrados_externos = fields.Text(string='Daños Encontados')

    danos_encontrados_internos = fields.Text(string='Daños Encontados')

    priority = fields.Selection([('0', 'Baja'),('1', 'Media'),('2', 'Alta')],string='Prioridad')

    
    inv_accesorios_id = fields.Many2many('inventario.accesorios',string='Accesorios')

    articulo_valor = fields.Text(string='Articulos de valor reportados')

    inv_com_mecanicos_id = fields.Many2many('inventariocomponentes.mecanicos',string='Componentes mecánicos')

    fecha_entrega= fields.Datetime(string='Fecha prevista de entrega')

    asesor_atiende_id = fields.Many2one('res.partner',string='Asesor que atiende')

    total=fields.Float(string="Total")

    diagnostico = fields.Text(string='Diagnóstico')

    recome_entrega=fields.Text(string='Recomendaciones')

    createorder = fields.Boolean(string='create orden')

    tarifa_id = fields.Many2one(
        'product.pricelist',
        string='Tarifa',
    )

    base_imponible = fields.Float(
        string='Base imponible',
    )

    impuestos = fields.Float(
        string='Impuestos',
    )


    orden_garantia_id = fields.Many2one(
        'sale.order',
        string='Orden Garantia',
    )


    lista_liqudo_fluido_ids = fields.One2many(
        'ck_liquido.fluido',
        'lista_id',
        string='liquido Fluido',
    )

    lista_luces_ids = fields.One2many(
        'ck_luces',
        'lista_id',
        string='Luces',
    )
    lista_inp_vin_ids = fields.One2many(
        'ck_inspeciones_vis',
        'lista_id',
        string='Inspecciones Visibles y Funcionales',
    )
    lista_fdd = fields.One2many(
        'ck_neumaticos.frenos_delante_de',
        'lista_id',
        string='Neumáticos y Frenos delantero Derecho',
    )

    lista_fdi = fields.One2many(
        'ck_neumaticos.frenos_delante_izq',
        'lista_id',
        string='Neumáticos y Frenos delantero Izquierdo',
    )
    lista_ftd = fields.One2many(
        'ck_neumaticos.frenos_trasero_der',
        'lista_id',
        string='Neumáticos y Frenos Trasero Derecho',
    )
    lista_fti = fields.One2many(
        'ck_neumaticos.frenos_trasero_izq',
        'lista_id',
        string='Neumáticos y Frenos Trasero Izquierdo',
    )


    puesto_psi0 = fields.Char(
        string='Puesto a',
    )
    puesto_psi1 = fields.Char(
        string='Puesto a',
    )
    puesto_psi2 = fields.Char(
        string='Puesto a',
    )
    puesto_psi3 = fields.Char(
        string='Puesto a',
    )

    numer_motor = fields.Char(
        string='Numero de motor',
    )

    def _set_fecha_calendar(self):
        cita_ids=self.env['calendar.event'].search([('order_repar_id','=',self.id)],limit=1)
        for item in self:
            if cita_ids.allday:
                item.fecha_proximo_servicio=cita_ids.start_date
            else:
                item.fecha_proximo_servicio=cita_ids.start_datetime

   

    fecha_proximo_servicio = fields.Datetime(
        string='Proximo Servicio',
        compute="_set_fecha_calendar"
    )
    kilometraje_maximo_proximo = fields.Float(
        string='Kilometraje maximo para proximo servicio',
    )

    currency_id = fields.Many2one(
        'res.currency',
        string='currency',
    )
    

    def calcular_productos(self):        
        if self.cosume_part_ids:
            aux=0.0
            for item in self.cosume_part_ids:
                aux+=item.costo*item.qty    
                    
            tax=self.env['car_repair.tax'].search([],limit=1)   
            self.base_imponible=aux
            self.impuestos=self.base_imponible*tax.tax 
            self.total=self.base_imponible+(self.base_imponible*tax.tax)
            self.currency_id=tax.currency_id.id
        else:
            self.total=0.0
            self.base_imponible=0.0
            self.impuestos=0.0



    @api.onchange('cosume_part_ids')
    def _onchange_cosume_part_ids(self):
        self.calcular_productos()       
    
   
    def getdata_liquidos(self):
        liquidos=[]
        for item in self.env['liquido.fluido'].search([]):
            liquidos.append((0,0,{'nombre':item.id}))
        return liquidos
    def getdata_luces(self):
        luces=[]
        for item in self.env['luces'].search([]):
            luces.append((0,0,{'nombre':item.id}))
        return luces
    def getdata_inspvsfuncion(self):
        inspvsfuncion=[]
        for item in self.env['inspeciones.vis_funcion'].search([]):
            inspvsfuncion.append((0,0,{'nombre':item.id})) 
        return inspvsfuncion
    def getdata_nuem_fdd(self):
        nuem_fdd=[]
        for item in self.env['neumaticos.frenos_delante_de'].search([]):
            nuem_fdd.append((0,0,{'nombre':item.id}))
        return nuem_fdd
    def getdata_nuem_fdi(self):
        nuem_fdi=[]
        for item in self.env['neumaticos.frenos_delante_izq'].search([]):
            nuem_fdi.append((0,0,{'nombre':item.id}))
        return nuem_fdi
    def getdata_nuem_ftd(self):
        nuem_ftd=[]
        for item in self.env['neumaticos.frenos_trasero_der'].search([]):
            nuem_ftd.append((0,0,{'nombre':item.id}))
        return nuem_ftd
    def  getdata_nume_fti(self):
        nume_fti=[]
        for item in self.env['neumaticos.frenos_trasero_izq'].search([]):
            nume_fti.append((0,0,{'nombre':item.id}))
        return nume_fti

    @api.model 
    def default_get(self,fields):
        res=super(Auto_usuario_cliente_repair,self).default_get(fields)
        clausula=self.env['car_repair.clausula'].search([],limit=1).clausula
    
        res.update({
            'asesor_atiende_id':self.env.user.partner_id.id or False,
            'lista_liqudo_fluido_ids':self.getdata_liquidos() or False,
            'lista_luces_ids':self.getdata_luces() or False,
            'lista_inp_vin_ids':self.getdata_inspvsfuncion() or False,
            'lista_fdd':self.getdata_nuem_fdd() or False,
            'lista_fdi':self.getdata_nuem_fdi() or False,
            'lista_ftd':self.getdata_nuem_ftd() or False,
            'lista_fti':self.getdata_nume_fti() or False,
            'clausula':clausula,

        })

        return res

    odometro_actual = fields.Integer(string='Kilometraje actual')

    credencial_numeros = fields.Char(string='Credencial')

    foto_credencial = fields.Binary(string='Documento',attachment=True)

    res_val_estado = fields.Boolean(string='Estado ')
   

    @api.onchange('team_id','tipo_servicio')
    def load_responsable_id(self):
        if self.team_id:            
            list_responsable=[]
            #filtro
            responsable_usuarios=self.env['car.support.team'].search([('id','=',self.team_id.id)])
            for item in responsable_usuarios.team_ids:
                list_responsable.append(item.id)      
            self.res_val_estado=True     
            return {'domain':{'user_id':[('id','=',list_responsable)]}}

    @api.onchange('user_id')
    def _onchange_user_id(self):
        if self.user_id:            
            busqueda=self.env['etapas.reparacion'].search([('value','=','new')],limit=1)
            self.state=busqueda.proxima_estapa_id.value
            self.stage_id=busqueda.proxima_estapa_id.id
    


    def set_to_close(self):
        if self.is_close != True:
            self.is_close = True
            self.close_date = fields.Datetime.now()#time.strftime('%Y-%m-%d')
            self.state = 'closed'
            template = self.env.ref('car_repair_maintenance_service.email_template_car_ticket1')
            template.send_mail(self.id)
            factura=self.env['account.move'].search([('invoice_origin','=',self.origen_reparacion.name)])
            if factura.state!='posted':
                raise UserError("La factura esta en borrador")  

            self.env['fleet.vehicle.log.services'].create({
            'vehicle_id':self.flota_cliente.id,
            'odometer':self.kilometraje,
            'amount':self.total,
            'cost_subtype_id':self.tipo_servicio.servicio_flota.id,
            'orden_servicio':self.id,
            'date':self.close_date, 
            'vendor_id':self.partner_id.id,
            'purchaser_id':self.company_id.partner_id.id,
            'inv_ref':factura.name,
            'notes':self.nature_of_service_id.name
             })
            cierre=self.env['etapas.reparacion'].search([('value','=','closed')],limit=1)
            self.stage_id=int(cierre.sequence)         



    @api.onchange('state')
    def _onchange_state(self):
        for rec in self:
            
            if rec.state:
                id_states=self.env['etapas.reparacion'].search([('value','=',rec.state)])#.sequence            
                if len(id_states)<=1:
                    rec.stage_id=int(id_states.sequence)
                else:
                    raise UserError("Revisa las etapas")
             
    
    lista_danos_internos_ids = fields.One2many(
        'danos.interiorck',
        'lista_danos_interior_id',
        string='Daños Internos',
    )

    lista_danos_externos_ids = fields.One2many(
        'danos.exterioresck',
        'lista_danos_exterio_id',
        string='Daños Externos',
    )

    @api.constrains('lista_danos_internos_ids')
    def _exite_dano_internos(self):
        for rec in self:
            existe_reacord_lines=[]
            for line in rec.lista_danos_internos_ids:
                if not line.danos_interior_id.id:
                    raise ValidationError("Un campo esta vacio de daños internos")
                if line.danos_interior_id.id in existe_reacord_lines:                    
                    raise ValidationError("Exite un daños repetido en interno")
                existe_reacord_lines.append(line.danos_interior_id.id)

    @api.constrains('lista_danos_externos_ids')
    def _exite_dano_externos(self):
        for rec in self:
            existe_reacord_lines=[]
            for line in rec.lista_danos_externos_ids:
                if not line.danos_exterior_id.id:
                    raise ValidationError("Un campo esta vacio de daños externos")
                if line.danos_exterior_id.id in existe_reacord_lines:
                    raise ValidationError("Exite un daños repetido en externos")
                existe_reacord_lines.append(line.danos_exterior_id.id)

 
    @api.model
    def _get_status_list(self):        
        selection_list=[]
        selection=self.env['etapas.reparacion'].search([])
        for item in selection:
            selection_list.append((item.value,item.name))
        return selection_list 


    state=fields.Selection(selection=_get_status_list,string="state")


    @api.onchange('nature_of_service_id')
    def _onchange_nature_of_service(self):
        self.subject=self.nature_of_service_id.name
        for item in self.cosume_part_ids:
            if item.auto_selec and not item.presupuestado_id:
                self.write({'cosume_part_ids':[(2,item.id,0)]})       

        if self.nature_of_service_id:            
            for item in self.nature_of_service_id.tablas_de_producto:
                self.write({
                    'cosume_part_ids':[(0,0,{
                                'product_id':item.productoservicio_id.id,
                                'qty':item.cantidad,
                                'costo':item.productoservicio_id.lst_price,
                                'product_uom':item.unidades.id,
                                'auto_selec':True,
                            })]
                })
        self.get_tarifas_product()

    @api.onchange('field_filter')
    def _onchange_field_filter(self):

        if self.field_filter:
            temp=self.field_filter
            domain_economica=[('numero_economico','=',temp)]
            domain_placa=[('license_plate','=',str(temp).upper())]
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
    

    @api.onchange("odometro_actual")
    def actualizar_kilometros(self):
        if self.odometro_actual>=self.kilometraje:
            self.kilometraje=self.odometro_actual
            self.env['fleet.vehicle'].search([('id','=',self.flota_cliente.id)]).update(
                {'odometer':self.odometro_actual})
        else:
            raise UserError("El nuevo kilometraje debe ser mayor")

    @api.onchange('damage')
    def actualizar_dano(self):
        self.env['fleet.vehicle'].search([('id','=',self.flota_cliente.id)]).update(
            {'danos_preexistentes':self.damage})


    origen_reparacion = fields.Many2one('sale.order',string='Origen')

    origen_cambio = fields.Boolean(string='Cambio origen')

    @api.onchange('origen_cambio')
    def load_presupuestos(self):
        for rec in self:
            if rec.origen_cambio:
                list_origen=[]  
                context=self.env.context.get('params')            
                origen_list=self.env['sale.order'].search([('repair_origin_id','=',self._origin.id)])           

                for item in origen_list:
                    list_origen.append(item.id)
                if list_origen:
                    return {'domain':{'origen_reparacion':[('id','=',list_origen)]}}
                else:
                    return {'domain':{'origen_reparacion':[('id','=',[])]}}
                

    
    transmision = fields.Selection(
        string="Tipo de transmisión",
        selection=[
                ('Automatica', 'Automatica'),
                ('Manual', 'Manual'),
        ],
    )

    kilometraje = fields.Integer(string="Kilometraje")

    tipo_motor = fields.Char(string="Tipo de motor")

    uom_oum = fields.Selection(
        string="Unidades",
        selection=[
                ('Kilometros', 'Kilometros'),
                ('Millas', 'Millas'),
        ],
    )

    valida_cliente = fields.Boolean(string='v cliente',default='True')

    valida_autos = fields.Boolean(string='v autos',default='True')

    @api.onchange('tipo_servicio')
    def load_clientes(self):
        if self.tipo_servicio:            
            list_users=[]
            users_list=self.env['res.partner'].search([('dueno_autos','=',True)])

            for item in users_list:
                list_users.append(item.id)

            self.valida_cliente=False

            return {'domain':{'partner_id':[('id','=',list_users)]}}
    

    @api.onchange('partner_id')
    def load_clientes_autos(self):
        if self.partner_id:
            list_autos=[] 
            self.tarifa_id=self.partner_id.property_product_pricelist.id          
 
            auto_clientes=self.env['fleet.vehicle'].search([('cliente','=',self.partner_id.id)])

            for item in auto_clientes:
                list_autos.append(item.id)

            self.valida_autos=False

            return {'domain':{'flota_cliente':[('id','=',list_autos)]}}

    
    count_reg=fields.Integer(compute="_calculo_registro")

    def _calculo_registro(self):
       for rec in self:
           rec.count_reg=self.env['sale.order'].search_count([('repair_origin_id','=',rec.id)])

    count_reg_fac=fields.Integer(compute="_calculo_registro_factura")

    def _calculo_registro_factura(self):
       for rec in self:
           rec.count_reg_fac=self.env['account.move'].search_count([('repair_origin_id','=',rec.id)])

    def create_order_quo(self):
        for rec in self:
            count_row=0
            for line in rec.cosume_part_ids:
                count_row=count_row+1
            if count_row==0:
                raise UserError("Favor de agregar por lo menos un producto o servicio para crear presupuesto")        
            
        order_new=self.env['sale.order'].create({
        'partner_id':self.partner_id.id,
        'flota_cliente':self.flota_cliente.id,
        'motivo':self.tipo_servicio.id,
        'user_id':self.env.user.id,
        'repair_origin_id':self.id,
        'fecha_entrega':self.fecha_entrega,
        'numero_serie':self.numero_serie,
        'odometroactual':self.odometro_actual,
        'atendio_id':self.asesor_atiende_id.id,
        'order_creada':True,
        })
        self.origen_reparacion=order_new.id         
        for list_item in self.cosume_part_ids:
            if not list_item.presupuestado_id:
                producto=self.env['product.product'].search([('id','=',list_item.product_id.id)])
                list_data={
                   'order_line':[(0,0,{
                             'product_id':producto.id,
                             'product_uom_qty':list_item.qty,
                             'price_unit':producto.lst_price,
                             'name':producto.name,
                             'product_uom':producto.uom_id.id,
                    })]
                }                
                order_new.write(list_data)
                self.write({
                        'cosume_part_ids':[(1,list_item.id,{
                                'presupuestado_id':self.origen_reparacion.id,                                
                            })]
                        })      
        

       

    #crear historial de servicio por automivil
    def create_servicio_automovil(self):
        self.env['fleet.vehicle.log.services'].create({
            'vehicle_id':self.flota_cliente.id,
            'cos_sutype_id':self.tipo_servicio.id,
            'odometer':self.kilometraje            
            })  
        

    @api.onchange("flota_cliente")
    def load_auto_cliente(self):

        transmision={'manual':'Manual','automatic':'Automatica'}

        tran_uom={'kilometers':'Kilometros','miles':'Millas'}

        combutible={'gasoline':'Gasolina',
                    'diesel':'Diesel',
                    'lpg':'GLP',
                    'eletric':'Eléctrico',
                    'hybrid':'Hibrido'}

        for recod in self:

            load_transmision=''
            if self.flota_cliente.transmission:
                load_transmision=transmision[self.flota_cliente.transmission]
            
            load_tran_uom=''
            if self.flota_cliente.odometer_unit:
                load_tran_uom=tran_uom[self.flota_cliente.odometer_unit]
            
            fuel_tipo=''
            if self.flota_cliente.fuel_type:
                fuel_tipo=combutible[self.flota_cliente.fuel_type]

            it_catg=[]

            for item in recod.flota_cliente.tag_ids:
                it_catg.append(item.id)


            if recod.flota_cliente:
                recod.phone=recod.partner_id.phone
                recod.email=recod.partner_id.email
                recod.numero_serie=recod.flota_cliente.vin_sn
                recod.year=recod.flota_cliente.model_year
                recod.brand=recod.flota_cliente.model_id.brand_id.name
                recod.placa=recod.flota_cliente.license_plate
                recod.color=recod.flota_cliente.color
                recod.kilometraje=recod.flota_cliente.odometer
                recod.transmision=load_transmision
                recod.uom_oum=load_tran_uom
                recod.linea=recod.flota_cliente.linea
                recod.tipo_motor=recod.flota_cliente.fuel_type
                recod.img_auto=recod.flota_cliente.img_auto
                recod.categoria_ids=it_catg
                recod.damage=recod.flota_cliente.danos_preexistentes
                recod.numero_economico=recod.flota_cliente.numero_economico
                recod.conductor=recod.flota_cliente.driver_id.id
                recod.numer_motor=recod.flota_cliente.numero_motor
                recod.puesto_conductor=recod.flota_cliente.driver_id.function
                recod.titulo_conductor=recod.flota_cliente.driver_id.title.name
                recod.telefono_conductor=recod.flota_cliente.driver_id.phone
                recod.email_conducto=recod.flota_cliente.driver_id.email
                recod.model=recod.flota_cliente.model_id.brand_id.name+"/"+recod.flota_cliente.model_id.name
                data_cred=self.env['fleet.vehicle.assignation.log'].search([('driver_id','=',self.conductor.id)],limit=1)
                recod.credencial_numeros=data_cred.Credencia
                recod.foto_credencial=data_cred.Imagen_credencia
    
    def update_qr(self):
        self._generate_qr()
        self._generar_url()

    def _generar_url(self):
        link=self.get_base_url() + "/my/repair_request/"+str(self.name.lower())+"-"+str(self.id)
        self.url=link


    def _generate_qr(self):
        link=self.get_base_url() + "/my/repair_request/"+str(self.name.lower())+"-"+str(self.id)
        self.url=link
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(self.url)
        qr.make(fit=True)
        img = qr.make_image()
        temp = BytesIO()
        img.save(temp, format="PNG")
        qr_image = base64.b64encode(temp.getvalue())
        self.qr_code=qr_image

        #display_msg="""<strong style="color:green">El QR ha sido genedaro</strong> """
        #self.sudo().message_post(body=display_msg,subject="Accion de QR")

    qr_code = fields.Binary(string="QR code",attachment=True,compute='_generate_qr')

    url = fields.Char(string='Enlace',compute='_generar_url')

    tipo_medidad_aire0 = fields.Selection([('0','PSI'),('1', 'LIBRAS')],string='Tipo')

    tipo_medidad_aire1 = fields.Selection([('0','PSI'),('1', 'LIBRAS')],string='Tipo')

    tipo_medidad_aire2 = fields.Selection([('0','PSI'),('1', 'LIBRAS')],string='Tipo')

    tipo_medidad_aire3 = fields.Selection([('0','PSI'),('1', 'LIBRAS')],string='Tipo')

    def get_model_id(self):
        return self.env['ir.model'].search([('model','=','car.repair.support')],limit=1).id
    
    def action_actividad_asesor(self):        
        users=self.env['res.users'].search([('partner_id','=',self.asesor_atiende_id.id)],limit=1).id
        self.env['mail.activity'].sudo().create({
            'res_model_id':self.get_model_id(),
            'res_id':self._origin.id,
            'res_model':'car.repair.support',
            'res_name':self.name,
            'activity_type_id':4,
            'summary':'Diagnóstico de auto',
            'date_deadline':self.request_date,
            'user_id':users, #res
            'note':self.diagnostico,

            })
        busqueda=self.env['etapas.reparacion'].search([('value','=','diagnosis')],limit=1)
        self.state='diagnosis'
        self.stage_id=int(busqueda.sequence)
            
    @api.onchange('state')
    def _onchange_state_validate(self):
        
        if self.state=='closed':
            factura=self.env['account.move'].search([('invoice_origin','=',self.origen_reparacion.name)])
            bandera=False
            for item in factura:
                if item.state!='posted':
                    bandera=False
                else:
                    bandera=False
            if not bandera:
                raise UserError("No existe factura publicada")

        if self.state=='assigned':
            if not self.user_id:
                raise UserError("Forma incorrecta de cambiar etapa")
        if self.state=='work_in_progress':
            raise UserError("Forma incorrecta de cambiar etapa")
       # if self.state=='new':
        #    raise UserError("Forma incorrecta de cambiar etapa")
        if self.state=='diagnosis':
            raise UserError("Forma incorrecta de cambiar etapa")

            # if not self.origen_reparacion:
            #     raise UserError("No cuentas con un presupuesto asignado")            
            # orden=self.env['sale.order'].search([('invoice_origin','=',self.origen_reparacion.name)])
            # bandera=False
            # for item in orden:
            #     if item.state!='done':
            #         bandera=False
            #     else:
            #         bandera=True
            # if not bandera:
            #     raise UserError("No existe presupuesto confimado")
            # else:
            #     raise UserError("No se puede hacer esta acción")

                

    def _set_cita_calendar(self):
        cita_ids=self.env['calendar.event'].search([('order_repar_id','=',self.id)],limit=1)       
        for item in self:
            item.cita_id=cita_ids.id

    cita_activa = fields.Boolean(
        string='cita_activa',
    )
    cita_cancelada = fields.Boolean(
        string='cancelada',
    )

    def action_listo_entrega(self):
         busqueda=self.env['etapas.reparacion'].search([('value','=','List_para_entrega')],limit=1)
         self.state='Listo_para_entrega'
         self.stage_id=busqueda.sequence


    def cancelar_actividad(self):
        cita_ids=self.env['calendar.event'].search([('order_repar_id','=',self.id)],limit=1)  
        cita_ids.unlink()
        self.cita_cancelada=True
        self.cita_activa=False
        

    cita_id = fields.Many2one('calendar.event',string='Cita',compute='_set_cita_calendar')

    def agendar_actividad(self):       
       
        try:
            view_id=self.env.ref("calendar.view_calendar_event_form").id
            context = self._context.copy()
        except Exception as e:
            view_id=False
        self.cita_activa=True
        self.cita_cancelada=False
        ctx={
          'default_name':self.flota_cliente.name,
          'default_allday':True,
          'default_order_repar_id':self.id,
        }

        return {
        'name':_("Proximo Servicio"),   
        'view_mode': 'form',
        'view_id': view_id,
        'view_type': 'form',
        'res_model': 'calendar.event',
        'type': 'ir.actions.act_window',
        'context': ctx,
        'target': 'new',
        }

    #aplicar tarifas a la line de productos
    @api.onchange('cosume_part_ids')
    def get_tarifas_product(self):        
        tarifa=self.tarifa_id.item_ids    

        for item in self.cosume_part_ids: 
            aux=0.0         
            for record in tarifa:
                if record.compute_price=='fixed':
                    aux+=item.costo+record.fixed_price
                if record.compute_price=='percentage':
                    aux+=(record.percent_price/100)*item.costo
                if record.compute_price=='formula':
                    aux+=(item.costo-(record.price_discount/100)*item.costo)+record.price_surcharge                
            if not tarifa:
                aux=item.costo                
            item.costo=aux        


    # @api.constrains('odometro_actual')
    # def _ceronull_odometro_actual(self):
    #     if self.odometro_actual<=0:
    #         raise UserError("El kilometraje actual debe ser mayor a 0") 


    def action_danos_product(self):

        for item in self.lista_danos_internos_ids:
            if not item.agregado_interior:                
                productos=self.env['danos.interior'].search([('id','=',item.danos_interior_id.id)]).productos_id                
                for list_item in productos:
                    self.write({
                            'cosume_part_ids':[(0,0,{
                                    'product_id':list_item.id,
                                    'costo':list_item.lst_price,
                                    'product_uom':list_item.uom_id.id,
                                    'auto_checks':True,
                                })]
                    })
                    self.write({
                            'lista_danos_internos_ids':[(1,item.id,{
                                    'agregado_interior':True,                                
                                })]
                            })

        for item in self.lista_danos_externos_ids:
            if not item.agregado_exterior:
                productos=self.env['danos.exteriores'].search([('id','=',item.danos_exterior_id.id)]).productos_id
                for list_item in productos:
                    self.write({
                            'cosume_part_ids':[(0,0,{
                                    'product_id':list_item.id,
                                    'costo':list_item.lst_price,
                                    'product_uom':list_item.uom_id.id,
                                    'auto_checks':True,
                                })]
                    })
                    self.write({
                            'lista_danos_externos_ids':[(1,item.id,{
                                    'agregado_exterior':True,                                
                                })]
                            })
        self.get_tarifas_product()
        self.calcular_productos()




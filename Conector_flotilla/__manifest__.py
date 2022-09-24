# -*- coding: utf-8 -*-
{
    'name': "Conector con flotilla",

    'summary': """
        Conecta el modulo de taller de reparacion con el modulo de flotilla para tener un listado de auto por usuario/cliente""",

    'description': """
        Agrega algunos campos faltantes para precargar de modulo de flotilla
        Precargar y los anteriores autos que ya han tenido un servicion 
        En conctactos cuentas con un listado o boton para ver todo los autos por usuario/cliente
    """,

    'author': "ogum",
    'website': "http://www.yourcompany.com",

    'category': 'Uncategorized',
    'version': '13.0.1',

    # any module necessary for this one to work correctly,
    'depends': ['base','car_repair_maintenance_service'],

    # always loaded
    'data': [
          'security/ir.model.access.csv',
          'views/parnert_button.xml',
          'views/crear_orden_reparacion.xml',
          'views/car_autos_car.xml',
          'views/flotas.xml',
          'views/lista_danos_interior.xml',
          'views/lista_danos_exterior.xml',
          'views/etapas_reparacion_view.xml',   
          'views/inventario_componentes.xml',
          'views/inventario_accesorios.xml',    
          'views/custom_invoice.xml',
          'views/custom_view_ventas.xml',
          'views/adjuntos_credenciales.xml',
          'data/grupo_menus_sinpermisos.xml',
          'views/custom_menu.xml',
          'views/check_entregadas.xml',
          'views/placas_historial.xml',
          'views/config_taxes.xml',
          'views/custom_view_ventas.xml',
          'data/estapas_estandar.xml',
          'views/templetaassent.xml',
          'views/customer_vehiculos_productos.xml',
          'views/custom_view_website.xml',
          'views/config_clausulas.xml',
          'views/cita_car_repair.xml',
          'views/resulta_check_list_entrega.xml', 
          'views/fabricacion_car_conector.xml',
          'report/papel_format_entegra.xml',
          'report/papel_format_recepcion.xml',
          'report/report_entrega.xml',
          'report/report_recepcion.xml',
          'data/currency.xml',
          'data/clausula_inicial.xml',
          'data/check_result_data.xml',
          'data/crear_categoria.xml',
    ],
}

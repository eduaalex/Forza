odoo.define('custom_car_repair_list_products', function (require) {
    "use strict";
    var ajax = require('web.ajax');

    $(document).on('change','#auto_cliente',function(){
          var values=$("#auto_cliente option:selected").val();          
          ajax.jsonRpc("/filter/product", 'call',{
            'auto':values
          }).then(function (data) {
              
              $("#data_autos").html(data['html_autos'])

              $("#data_autos").html(data['html_autos'])
              $("input[name='brand']").val(data['html_marca'])
              $("input[name='placa']").val(data['html_placa'])
              $("input[name='serie']").val(data['html_serie'])
              $("input[name='model']").val(data['html_modelo'])
              $("input[name='year']").val(data['html_ano'])

          });
    }); 
    
    
    $(document).on('click','.item_check_list',function(){   
       var marcados=[] 
       $("input:checkbox:checked").each(function(){
        
          marcados.push($(this).attr('id'))
         
       })  
        $("#salida_check").val(marcados)
        })
     


})

 


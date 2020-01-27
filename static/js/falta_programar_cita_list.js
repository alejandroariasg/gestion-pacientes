$(document).ready(function(){
    var table;
    table = $('#tabla_falta_programar_cita').DataTable({
        
        "fnDrawCallback": function( oSettings ) {
            angedar_paciente();
        },
        "oLanguage": {
            "sProcessing":     "Cargando...",
            "sZeroRecords":    "No se encontraron resultados",
            "sEmptyTable":     "Ningún dato disponible en esta tabla",
            "sInfo":           "Mostrando del (_START_ al _END_) de un total de _TOTAL_ registros",
            "sInfoEmpty":      "Mostrando del 0 al 0 de un total de 0 registros",
            "sInfoFiltered":   "(filtrado de un total de _MAX_ registros)",
            "sInfoPostFix":    "",
            "sSearch":         "Filtrar:",
            "sUrl":            "",
            "sInfoThousands":  ",",
            "sLoadingRecords": "Por favor espere - cargando...",
            "oPaginate": {
                "sFirst":    "Primero",
                "sLast":     "Último",
                "sNext":     "Siguiente",
                "sPrevious": "Anterior"
            },
            "oAria": {
                "sSortAscending":  ": Activar para ordenar la columna de manera ascendente",
                "sSortDescending": ": Activar para ordenar la columna de manera descendente"
            }
        }
    });

    function angedar_paciente(){
        $('#tabla_falta_programar_cita tbody').on( 'click', '.agendar', function (){
            id = this.id;
            $.ajax({
                url: "falta_programar_cita_listar_paciente",
                type: "GET",
                data: {'id' : id},
                success: function(data){
                    data = jQuery.parseJSON(data['data'])[0]['fields'];
                    $("#agenda-nombre").val(data.nombre);
                    $("#agenda-prim-apellido").val(data.primer_apellido);
                    $("#agenda-seg-apellido").val(data.segundo_apellido);
                    $("#agenda-numero-documento").val(data.numero_documento);
                    $("#agenda-telefono").val(data.telefono);
                    $("#agenda-dx").val(data.dx);
                    $("#agenda-paciente-id").val(id);
                    $('#modalAngendar').modal('show');	  	
                },
                error: function(result) {
                  console.log(result);
                }		
          });
        });
    }
})
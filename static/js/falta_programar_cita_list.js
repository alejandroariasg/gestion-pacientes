$(document).ready(function(){
    var table;
    table = $('#tabla_falta_programar_cita').DataTable({
        
        "fnDrawCallback": function( oSettings ) {
            angedar_paciente();
            cambiarDia();
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

    $('#agendar').click(function(){
		var nombre = $("#agenda-nombre").val()+" "+$("#agenda-prim-apellido").val()+" "+$("#agenda-seg-apellido").val();
		var fecha = $("#agenda-fecha").val()+" "+$("#agenda-hora").val();
		var dia =  $("#agenda-dia").val();
		var medico =  $("#agenda-persona-evalua").val();

		Swal.fire({
		  title: 'Esta seguro?',
		  text: "Desea agendar al paciente "+nombre+" para la fecha "+fecha+" día "+dia+" con el médico "+medico,
		  type: 'warning',
		  showCancelButton: true,
		  confirmButtonClass: "btn-success",
		  confirmButtonText: "Si, agendar",
		  cancelButtonText: "No, cancelar!",
		  closeOnConfirm: false,
		  closeOnCancel: false,
		  reverseButtons: true
		}).then((result) => {
		  if (result.value) {
		  	//var index_row = $("#agenda-index-row").val();
		  	var serializedData = $("#form-angedar").serialize()+ "&agenda-numero-documento=" + $("#agenda-numero-documento").val()+"&agenda-prim-apellido=" + $("#agenda-prim-apellido").val()+"&agenda-seg-apellido=" + $("#agenda-seg-apellido").val()+"&agenda-procedencia=" + $("#agenda-procedencia").val()+"&agenda-dia=" + $("#agenda-dia").val();
			var request;
			request = $.ajax({
				  url: "falta_programar_cita_listar_agendar",
				  data: serializedData,
				  type: "POST",
				  success: function(data){
				  	if(data != 'error'){
				  			$("#form-angedar")[0].reset();
					  		Swal.fire(
						      'Angendado!',
						      "Se agendó correctamente el paciente "+nombre+".",
						      'success'
						    );
					  		$('#modalAngendar').modal('toggle');
					  		/*angedar_paciente();
					  		editar_paciente();
					  		descartar_paciente();
					  		$('#pruebaDataTable').dataTable().fnDestroy();
		    				listar_citas_consultas_externas();*/
		    				//updateRow(index_row, JSON.parse(data).data);
				  	}else{
				  		Swal.fire(
					      'Error!',
					      'Ha ocurrido un error. Verifique que los campos estén correctamente diligenciados',
					      'error'
					    );
				  	}
				  	
				  },
				  error: function(result) {
                    console.log(result);
                  }		
		    	});
		  }
		});
	});


    function cambiarDia(){
		$( "#agenda-fecha" ).focusout(function() {
			var dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado","Domingo"];
			var date = new Date($('#agenda-fecha').val());
			$('#agenda-dia').val(dias[date.getDay()]);
		});
	}

})
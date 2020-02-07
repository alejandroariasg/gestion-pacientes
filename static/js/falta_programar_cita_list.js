$(document).ready(function(){
    var table;
    table = $('#tabla_falta_programar_cita').DataTable({
          "createdRow": function( row, data, dataIndex ) {
            $('td', row).eq(14).attr('id', 'estado_'+dataIndex);
        },
        "fnDrawCallback": function( oSettings ) {
            angedar_paciente();
            editar_paciente();
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
            var indexRow = table.row( $(this).closest('tr').index())[0][0];
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
                    $("#agenda-index-row").val(indexRow);
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
          var index_row = $("#agenda-index-row").val();
          var serializedData = $("#form-angedar").serialize()+ "&numero_documento=" + $("#agenda-numero-documento").val()+"&agenda-prim-apellido=" + $("#agenda-prim-apellido").val()+"&agenda-seg-apellido=" + $("#agenda-seg-apellido").val()+"&procedencia=" + $("#agenda-procedencia").val()+"&dia=" + $("#agenda-dia").val()+"&id_paciente_id=" + $("#agenda-paciente-id").val();
          var request;
          request = $.ajax({
              url: "falta_programar_cita_listar_agendar",
              data: serializedData,
              type: "POST",
              success: function(data){
                if(data.estatus == 'ok'){
                    $("#form-angedar")[0].reset();
                    Swal.fire(
                      'Angendado!',
                      "Se agendó correctamente el paciente "+nombre+".",
                      'success'
                    );
                    $('#modalAngendar').modal('toggle');
                    //location.reload();
                }else{
                  Swal.fire(
                    'Error!',
                    'Ha ocurrido un error '+data.estatus,
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

  function editar_paciente(){
      $('#tabla_falta_programar_cita tbody').on( 'click', '.editar', function (){
        id = this.id;
        var indexRow = table.row( $(this).closest('tr').index())[0][0];
        $.ajax({
          url: "falta_programar_cita_listar_paciente",
          data: {'id' : id},
          type: "GET",
          success: function(data){
            var data_agenda = jQuery.parseJSON(data['data'])[0]['fields'];
            console.log(data_agenda.fecha_hora);
            fecha = data_agenda.fecha_hora != null ? data_agenda.fecha_hora.split("T") : '';

            $("#nombre").val(data_agenda.nombre);
            $("#primer_apellido").val(data_agenda.primer_apellido);
            $("#segundo_apellido").val(data_agenda.segundo_apellido);
            $("#numero_documento").val(data_agenda.numero_documento);
            $("#telefono").val(data_agenda.telefono);
            $("#dx").val(data_agenda.dx);
            $("#lugar_residencia").val(data_agenda.lugar_residencia);
            $("#sexo").val($.trim(data_agenda.sexo));
            $("#edad").val(data_agenda.edad);
            $("#observaciones").val(data_agenda.observaciones);
            $("#fecha_hora").val(fecha[0]);
            $("#pisquitra").val(data_agenda.psiquiatra);
            $("#dia").val(data_agenda.dia);
            $("#update_paciente-id").val(id);
            $("#update_row_id").val(indexRow);

            //$('.selectpicker').selectpicker('refresh');
            $('#myModalUpdate').modal('show'); 			  	
          },
          error: function(result) {
            alert("Data not found"+result);
          }		
        });

    });
  }

  $('#editar').click(function(){
		var nombre = $("#nombre").val()+" "+$("#primer_apellido").val()+" "+$("#segundo_apellido").val();

		if($('#numero_documento').val() == ''){
			$( "#numero_documento" ).focus();
			Swal.fire(
		      'Alerta!',
		      'Por favor ingresa la cédula del paciente!',
		      'warning'
		    );
		}else if($('#nombre').val() == '' || $('#primer_apellido').val() == '0' || $('#segundo_apellido').val() == '0'){
			$( "#nombre" ).focus();
			Swal.fire(
		      'Alerta!',
		      'Por favor ingrese correctamente los nombres y apellidos del paciente!',
		      'warning'
		    );
		}else{
			Swal.fire({
			  title: 'Esta seguro?',
			  text: "Desea actualizar los datos el paciente "+nombre+".?",
			  type: 'warning',
			  showCancelButton: true,
			  confirmButtonClass: "btn-success",
			  confirmButtonText: "Si, editar",
			  cancelButtonText: "No, cancelar!",
			  closeOnConfirm: false,
			  closeOnCancel: false,
			  reverseButtons: true
			}).then((result) => {
				if (result.value) {
				var llamada = $('#update_llamada').prop('checked') ? "SI" : "NO";
        var serializedData = $("#form-editar").serialize()+ "&id=" + $("#update_paciente-id").val()+ "&dia=" + $("#update_dia").val()+ "&llamada=" + llamada;
				var request;
				var index_row = $("#update_row_id").val();
				request = $.ajax({
					  url: "falta_programar_cita_actualizar_paciente",
					  data: serializedData,
					  type: "POST",
					  success: function(data){
					  	if(data.estatus == 'ok'){
					  		$("#form-editar")[0].reset();
					  		Swal.fire(
						      'Datos actualizados!',
						      "Se han actualizado correctamente los datos del paciente "+nombre+".",
						      'success'
						    );
                $('#myModalUpdate').modal('toggle');
                location.reload();
					  		/*$('#pruebaDataTable').dataTable().fnDestroy();
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
	                    console.log("Data not found"+result);
	                  }		
			    	});
			  }
			});
		}
	});

  function cambiarDia(){
		$( "#agenda-fecha" ).focusout(function() {
			var dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado","Domingo"];
			var date = new Date($('#agenda-fecha').val());
			$('#agenda-dia').val(dias[date.getDay()]);
		});
	}

})
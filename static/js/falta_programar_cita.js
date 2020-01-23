$(document).ready(function(){
	$('#fform_cita').submit(function(e){
		e.preventDefault();
		
		var date = new Date();
		fecha_creacion = date.getFullYear()+'-'+date.getMonth()+1+'-'+date.getDate()+' '+date.getHours()+':'+date.getMinutes();
		fecha_actualizacion = date.getFullYear()+'-'+date.getMonth()+1+'-'+date.getDate();

		serialize_data = $(this).serialize()+'&fecha_creacion='+fecha_creacion+'&fecha_actualizacion='+fecha_actualizacion+'&estado='+1;
		console.log(serialize_data);
		$.ajax({
			url: $(this).attr("action"),
			type: $(this).attr("method"),
			data: serialize_data,

			success : function(json){
				console.log(json);
			}
		})
	})
})
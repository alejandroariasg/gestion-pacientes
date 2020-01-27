$(document).ready(function(){
	
	cambiarDia();
	
	function cambiarDia(){
		$( "#fecha_hora" ).focusout(function() {
			var dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado","Domingo"];
			var date = new Date($('#fecha_hora').val());
			$('#dia').val(dias[date.getDay()]);
		});
	}
})
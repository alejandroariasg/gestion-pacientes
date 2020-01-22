from django import forms
from apps.falta_programar_cita.models import FaltaProgramarCita

class FaltaProgramarCitaForm(forms.ModelForm):
	class Meta:
		model = FaltaProgramarCita

		fields = [
			'numero_documento',
			'nombre',
			'primer_apellido',
			'segundo_apellido',
			'dx',
			'telefono',
			'lugar_residencia',
			'observaciones',
			'fecha_hora',
			'psiquiatra',
			'fecha_creacion',
			'fecha_actualizacion',
			'sexo',
			'edad',
			'dia',
			'estado',
		]

		labels = {
			'numero_documento' : 'Número de documento',
			'nombre' : 'Nombre',
			'primer_apellido' : 'Primer apellido',
			'segundo_apellido' : 'Segundo apellidos',
			'dx' : 'DX',
			'telefono': 'Teléfono',
			'lugar_residencia' : 'Lugar de residencia',
			'observaciones' : 'Observaciones',
			'fecha_hora': 'Fecha cita',
			'psiquiatra' : 'Psiquiatra',
			'fecha_creacion' : 'Fecha creación',
			'fecha_actualizacion' : 'Fecha actualización',
			'sexo' : 'Sexo',
			'edad' : 'Edad',
			'dia' : 'Día',
			'estado' : 'Estado',
		}
		widgets = {
			'numero_documento' : forms.TextInput(attrs={'class':'form-control'}),
			'nombre' : forms.TextInput(attrs={'class':'form-control'}),
			'primer_apellido' : forms.TextInput(attrs={'class':'form-control'}),
			'segundo_apellido' : forms.TextInput(attrs={'class':'form-control'}),
			'dx' : forms.TextInput(attrs={'class':'form-control'}),
			'telefono':  forms.TextInput(attrs={'class':'form-control'}),
			'lugar_residencia' : forms.TextInput(attrs={'class':'form-control'}),
			'observaciones' : forms.Textarea(attrs={'class':'form-control'}),
			'fecha_hora':  forms.DateTimeInput(attrs={'class':'form-control'}),
			'psiquiatra' : forms.TextInput(attrs={'class':'form-control'}),
			'fecha_creacion' : forms.TextInput(attrs={'class':'form-control'}),
			'fecha_actualizacion' : forms.TextInput(attrs={'class':'form-control'}),
			'sexo' : forms.TextInput(attrs={'class':'form-control'}),
			'edad' : forms.NumberInput(attrs={'class':'form-control'}),
			'dia' : forms.TextInput(attrs={'class':'form-control'}),
			'estado' : forms.TextInput(attrs={'class':'form-control'}),
		}

from django import forms
from apps.falta_programar_cita.models import FaltaProgramarCita, Agenda

class FaltaProgramarCitaForm(forms.ModelForm):
	class Meta:
		model = FaltaProgramarCita
		ordering = ['-id']
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
	class AgendaForm(forms.ModelForm):
		model = Agenda
		fields = [
			'numero_documento',
			'fecha',
			'dia',
			'codigo_paisa',
			'hermanos',
			'persona_evalua',
			'fecha_actualizacion',
			'observaciones',
			'hospitalizado',
			'codigo_alternativo',
			'procedencia',
			'faltan_datos_red_cap',
			'estado',
		]
		labels = {
			'numero_documento' : 'Número documento',
			'fecha' : 'Fecha Cita',
			'dia' : 'Día cita',
			'codigo_paisa' : 'Código paisa',
			'hermanos' : 'Hermanos',
			'persona_evalua' : 'Persona que evalúa',
			'observaciones' : 'Observaciones',
			'hospitalizado': 'Hospitalizado',
			'codigo_alternativo': 'Código alternatívo',
			'procedencia' : 'Procedencia',
			'faltan_datos_red_cap' : 'Faltan campos RedCap',
		}
		widgets = {
			'numero_documento' : forms.TextInput(attrs={'class':'form-control'}),
			'fecha' : forms.DateTimeInput(attrs={'class':'form-control'}),
			'dia' : forms.TextInput(attrs={'class':'form-control'}),
			'codigo_paisa' : forms.TextInput(attrs={'class':'form-control'}),
			'hermanos' : forms.TextInput(attrs={'class':'form-control'}),
			'persona_evalua' : forms.TextInput(attrs={'class':'form-control'}),
			'observaciones' : forms.TextInput(attrs={'class':'form-control'}),
			'hospitalizado': forms.TextInput(attrs={'class':'form-control'}),
			'codigo_alternativo': forms.TextInput(attrs={'class':'form-control'}),
			'procedencia' : forms.TextInput(attrs={'class':'form-control'}),
			'faltan_datos_red_cap' : forms.TextInput(attrs={'class':'form-control'}),
		}

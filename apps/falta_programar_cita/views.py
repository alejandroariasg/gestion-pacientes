from django.shortcuts import render, redirect
from django.core import serializers
from django.http import HttpResponse, JsonResponse
from apps.falta_programar_cita.models import FaltaProgramarCita, Agenda
from django.views.generic import ListView
from apps.falta_programar_cita.forms import FaltaProgramarCitaForm, AgendaForm
from django.urls import reverse_lazy
import json


# Create your views here.
class FaltaProgramarCitaListar(ListView):
	model = FaltaProgramarCita
	template_name = 'falta_programar_cita/falta_programar_cita_list.html'
	paginate_by = 10

def FaltaProgramarCitaCreate(request):	
	if request.method == 'POST':
		form = FaltaProgramarCitaForm(request.POST)
		if form.is_valid():
			obj = form.save(commit=True)
			obj.fecha_creacion = '2020-01-01'
			obj.fecha_actualizacion = '2020-01-01'
			obj.estado = 1
			return redirect('falta_programar_cita:falta_programar_cita_listar')
		else:
			print(form.errors)
	else:
		form =FaltaProgramarCitaForm()
	return render(request, 'falta_programar_cita/falta_programar_cita_form.html', {'form':form})

def FaltaProgramarCitaListarPaciente(request):
	if request.method == 'GET':
		data = {
			'data' : serializers.serialize('json', FaltaProgramarCita.objects.raw('SELECT * FROM falta_programar_cita_faltaprogramarcita WHERE id = '+request.GET['id']))
		}
		return JsonResponse(data)
	else:
		return HttpResponse("ERROR!")

def Agendar(request):
	if request.method == 'POST':
		# CONSULTA PARA VALIDAR POSIBLES HERMANOS DE ACUERDO A LA COINCIDENCIA DE APELLIDOS
		id_paciente = request.GET['id']
		for p in FaltaProgramarCita.objects.raw("SELECT nombre, primer_apellido, segundo_apellido FROM falta_programar_cita_faltaprogramarcita WHERE id != "+id_paciente+" AND primer_apellido = "+request.GET['primer_apellido']+" AND segundo_apellido = "+request.GET['segundo_apellido']+" AND primer_apellido != '' and  segundo_apellido != '' "):
			nombre = p.nombre+' '+p.primer_apellido+' '+p.segundo_apellido
		print(nombre)
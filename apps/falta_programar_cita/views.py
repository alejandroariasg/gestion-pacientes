from django.shortcuts import render, redirect
from django.core import serializers
from django.http import HttpResponse, JsonResponse
from apps.falta_programar_cita.models import FaltaProgramarCita, Agenda
from django.views.generic import ListView
from apps.falta_programar_cita.forms import FaltaProgramarCitaForm, AgendaForm
from django.urls import reverse_lazy
import json
from datetime import date, datetime


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

def FaltaProgramarCitaAgendar(request):
	if request.method == 'POST':
		id_paciente = request.POST.get('id_paciente')
		prim_apellido = request.POST.get('agenda-prim-apellido')
		seg_apellido = request.POST.get('agenda-seg-apellido')
		hermanos = ''
		#CONSULTA PARA VALIDAR POSIBLES HERMANOS DE ACUERDO A LA COINCIDENCIA DE APELLIDOS
		for p in FaltaProgramarCita.objects.raw("SELECT id, nombre, primer_apellido, segundo_apellido FROM falta_programar_cita_faltaprogramarcita WHERE id != {} AND primer_apellido = '{}' AND segundo_apellido = '{}' AND primer_apellido != '' and  segundo_apellido != '' ".format(id_paciente, prim_apellido, seg_apellido)):
			hermanos += str('{} {} {} ,'.format(p.nombre, p.primer_apellido, p.segundo_apellido))
		
		form = AgendaForm(request.POST)
		if form.is_valid():
			obj = form.save(commit=True)
			obj.fecha = request.POST.get('fecha')+' '+request.POST.get('fecha_hora')
			obj.fecha_actualizacion = date.today()
			obj.hermamos = hermanos
			obj.estado = 1
			obj.id_paciente = FaltaProgramarCita.objects.get(id=id_paciente)
			obj.save()
		else:
			print(form.errors)

	return HttpResponse(request.POST.get('fecha_hora'))
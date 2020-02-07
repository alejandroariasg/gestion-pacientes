from django.shortcuts import render, redirect
from django.core import serializers
from django.http import HttpResponse, JsonResponse
from apps.falta_programar_cita.models import FaltaProgramarCita, Agenda
from django.views.generic import ListView
from apps.falta_programar_cita.forms import FaltaProgramarCitaForm, AgendaForm
from django.urls import reverse_lazy
import json
from django.db.models import Case, When, F
from datetime import date, datetime
from django.utils import timezone
from django.db import IntegrityError

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
			obj.fecha_actualizacion = timezone.now()
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
		form = AgendaForm(request.POST)
		if form.is_valid():
				obj = form.save(commit=True)
				id_paciente = request.POST.get('id_paciente')
				prim_apellido = request.POST.get('agenda-prim-apellido')
				seg_apellido = request.POST.get('agenda-seg-apellido')
				hermanos = ''
				#CONSULTA PARA VALIDAR POSIBLES HERMANOS DE ACUERDO A LA COINCIDENCIA DE APELLIDOS
				for p in FaltaProgramarCita.objects.raw("SELECT id, nombre, primer_apellido, segundo_apellido FROM falta_programar_cita_faltaprogramarcita WHERE id != {} AND primer_apellido = '{}' AND segundo_apellido = '{}' AND primer_apellido != '' and  segundo_apellido != '' ".format(id_paciente, prim_apellido, seg_apellido)):
    					hermanos += str('{} {} {} ,'.format(p.nombre, p.primer_apellido, p.segundo_apellido))
				print(request.POST.get('fecha'))
				print(request.POST.get('fecha_hora'))
				obj.fecha = request.POST.get('fecha')+' '+request.POST.get('fecha_hora')
				obj.fecha_actualizacion = date.today()
				obj.hermamos = hermanos
				obj.estado = 1
				obj.id_paciente = FaltaProgramarCita.objects.get(id=id_paciente)
				try:
					obj.save()
					paciente = FaltaProgramarCita.objects.get(id=id_paciente)
					paciente.estado = Case(
						When(estado=2, then=1),
						When(estado=3, then=1),
						default=(4),
					)
					paciente.dx = request.POST.get('agenda-dx')
					paciente.save()
				except IntegrityError as ie:
					print(ie.message)
					return JsonResponse({'estatus':ie.message})
				except ValueError as ve:
					print(ve.message)
					return JsonResponse({'estatus':ve.message})
		else:
			print(form.errors)
			return JsonResponse({'estatus':form.errors})

	return JsonResponse({'estatus':'ok'})
	
def FaltaProgramarCitaUpdate(request):
	if request.method == 'POST':
		cita = FaltaProgramarCita.objects.get(id=request.POST.get('id'))
		fecha_creacion = cita.fecha_creacion
		estado = cita.estado
		form_cita_update = FaltaProgramarCitaForm(request.POST or None, instance=cita)
		if form_cita_update.is_valid():
			obj = form_cita_update.save(commit=True)
			print(obj.fecha_creacion)
			obj.fecha_creacion = fecha_creacion
			obj.fecha_actualizacion = timezone.now()
			obj.estado = estado
			obj.save()
			return JsonResponse({'estatus':'ok'})
		else:
    			return JsonResponse({'estatus':form_cita_update.errors})

def FaltaProgramarCitaDiscard(request):
	if request.method == 'POST':
		try:
			print(request.POST.get('tipo-descarte'))
			paciente = FaltaProgramarCita.objects.get(id=request.POST.get('id_paciente'))
			paciente.estado = request.POST.get('tipo-descarte')
			paciente.observaciones = request.POST.get('descartar-observaciones')
			paciente.save()
		except IntegrityError as ie:
			print(ie.message)
			return JsonResponse({'estatus':ie.message})
		except ValueError as ve:
				print(ve.message)
				return JsonResponse({'estatus':ve.message})
	return JsonResponse({'estatus':'ok'})
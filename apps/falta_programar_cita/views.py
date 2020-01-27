from django.shortcuts import render, redirect
from django.core import serializers
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from apps.falta_programar_cita.models import FaltaProgramarCita
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from apps.falta_programar_cita.forms import FaltaProgramarCitaForm
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
			'data' : serializers.serialize('json', FaltaProgramarCita.objects.filter(id=request.GET['id']))
		}
		#return HttpResponse(json.dumps(paciente), content_type='application/json')
		return JsonResponse(data)
	else:
		return HttpResponse("GET!")
	
	"""id_paciente = request.GET.get('id', None)
	paciente = FaltaProgramarCita.objects.filter(id=id_paciente)
	return HttpResponse(json.dumps(paciente), content_type='application/json')"""
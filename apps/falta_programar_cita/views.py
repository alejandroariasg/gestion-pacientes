from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from apps.falta_programar_cita.models import FaltaProgramarCita
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from apps.falta_programar_cita.forms import FaltaProgramarCitaForm
from django.urls import reverse_lazy
import datetime


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
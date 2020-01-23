from django.shortcuts import render
from apps.falta_programar_cita.models import FaltaProgramarCita
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from apps.falta_programar_cita.forms import FaltaProgramarCitaForm
from django.urls import reverse_lazy
# Create your views here.
class FaltaProgramarCitaListar(ListView):
    model = FaltaProgramarCita
    template_name = 'falta_programar_cita/falta_programar_cita_list.html'
    paginate_by = 2

class FaltaProgramarCitaCreate(CreateView):
	model = FaltaProgramarCita
	form_class = FaltaProgramarCitaForm
	template_name = 'falta_programar_cita/falta_programar_cita_form.html'
	success_url = reverse_lazy('falta_programar_cita:falta_programar_cita_listar')

from django.shortcuts import render
from apps.falta_programar_cita.models import FaltaPorgramarCita
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

# Create your views here.
class FaltaProgramarCitaListar(ListView):
    model = FaltaPorgramarCita
    template_name = 'falta_programar_cita/falta_programar_cita_list.html'
    paginate_by = 2
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
	
	def get(self, request, *args, **kwargs):
		context = {'form': FaltaProgramarCitaForm()}
		return render(request, 'falta_programar_cita/falta_programar_cita_form.html', context)
	
	def post(self, request, *args, **kwargs):
		form = FaltaProgramarCitaForm(request.POST)
		print('CREANDO REGISTRO...')
		print(form['fecha_actualizacion'])
		if form.is_valid():
			cita = form.save()
			cita.save()
			return HttpResponseRedirect(reverse_lazy('falta_programar_cita:falta_programar_cita_listar'))
		return render(request, 'falta_programar_cita/falta_programar_cita_form.html', {'form': form})

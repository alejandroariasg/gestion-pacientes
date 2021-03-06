from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from apps.falta_programar_cita.views import FaltaProgramarCitaListar,  FaltaProgramarCitaCreate, FaltaProgramarCitaListarPaciente, FaltaProgramarCitaAgendar, FaltaProgramarCitaUpdate, FaltaProgramarCitaDiscard

urlpatterns = [
    url(r'^listar', FaltaProgramarCitaListar.as_view(), name='falta_programar_cita_listar'),
    url(r'^nuevo$', FaltaProgramarCitaCreate, name='falta_programar_cita_crear'),
    url(r'^falta_programar_cita_listar_paciente/$', FaltaProgramarCitaListarPaciente, name='falta_programar_cita_listar_paciente'),
    url(r'^falta_programar_cita_listar_agendar$', FaltaProgramarCitaAgendar, name='falta_programar_cita_listar_agendar'),
    url(r'^falta_programar_cita_actualizar_paciente$', FaltaProgramarCitaUpdate, name='falta_programar_cita_actualizar_paciente'),
    url(r'^falta_programar_cita_descartar_paciente$', FaltaProgramarCitaDiscard, name='falta_programar_cita_descartar_paciente'),
]
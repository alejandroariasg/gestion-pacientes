from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from apps.falta_programar_cita.views import FaltaProgramarCitaListar,  FaltaProgramarCitaCreate

urlpatterns = [
    url(r'^listar', FaltaProgramarCitaListar.as_view(), name='falta_programar_cita_listar'),
    url(r'^nuevo$', FaltaProgramarCitaCreate, name='falta_programar_cita_crear'),
]
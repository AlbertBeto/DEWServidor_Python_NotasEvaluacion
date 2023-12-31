from django.shortcuts import render
from django.views.generic import ListView, DetailView
from programacion_didactica.models import Unidad
from programacion_didactica.models import InstEvaluacion, PondRA, PondCriterio, PondCritUD

# Create your views here.
# UD6.7.a Creo las views siguiendo tabla 1 de anexos III
class UnidadListView(ListView):
    model = Unidad
    template_name = 'programacion_didactica/unidad_list.html'
    
class UnidadDetailView(DetailView):
    model = Unidad
    template_name = 'programacion_didactica/unidad_detail.html'
    
class InstEvListView(ListView):
    model = InstEvaluacion
    template_name = 'programacion_didactica/ie_list.html'

class InstEvDetailView(DetailView):
    model = InstEvaluacion
    template_name = 'programacion_didactica/ie_detail.html'

class PondRAListView(ListView):
    model = PondRA
    template_name = 'programacion_didactica/pond_ra_list.html'
    
class PondRADetailView(DetailView):
    model = PondRA
    template_name = 'programacion_didactica/pond_ra_detail.html'
    
class PondCritListView(ListView):
    model = PondCriterio
    template_name = 'programacion_didactica/pond_ce_list.html'
    
class PondCritDetailView(DetailView):
    model = PondCriterio
    template_name = 'programacion_didactica/pond_ra_detail.html'
    
class PondCritUDListView(ListView):
    model = PondCritUD
    template_name = 'programacion_didactica/pond_ce_ud_list.html'

class PondCritUDDetailView(DetailView):
    model = PondCritUD
    template_name = 'programacion_didactica/pond_ce_ud_detail.html'
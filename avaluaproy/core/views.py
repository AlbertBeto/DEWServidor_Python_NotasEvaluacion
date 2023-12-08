from django.shortcuts import render
from django.views.generic import ListView, DetailView
from core.models import Modulo, ResAprendizaje, CritEvaluacion


class ModuloListView(ListView):
      # UD6.8.b En el view le digo cuanto elementos de la lista quiero que muestre con paginate_by
    paginate_by = 4
    model = Modulo
    template_name = 'core/modulo_list.html'


class ModuloDetailView(DetailView):
    model = Modulo
    template_name = 'core/modulo_detail.html'


class RAListView(ListView):
      # UD6.8.b En el view le digo cuanto elementos de la lista quiero que muestre con paginate_by
    paginate_by = 4
    model = ResAprendizaje
    template_name = 'core/ra_list.html'


class RADetailView(DetailView):
    model = ResAprendizaje
    template_name = 'core/ra_detail.html'


class CEListView(ListView):
     # UD6.8.b En el view le digo cuanto elementos de la lista quiero que muestre con paginate_by
    paginate_by = 6
    model = CritEvaluacion
    template_name = 'core/ce_list.html'


class CEDetailView(DetailView):
    model = CritEvaluacion
    template_name = 'core/ce_detail.html'

from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView, ListView, CreateView
from main_app.forms import AddItemForm


class IndexView(TemplateView):
    template_name = 'home.html'

class AddItemView(CreateView):
    form_class = AddItemForm
    success_url = reverse_lazy('time_line')
    template_name = 'add_item.html'

class TimeLineView(TemplateView):
    template_name = 'home.html'


# class AddCategoryView(CreateView):



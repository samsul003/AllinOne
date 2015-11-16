from django.core.urlresolvers import reverse_lazy
from django.utils import timezone
from django.forms import forms
from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView, ListView, CreateView, FormView, DeleteView
from main_app.forms import AddItemForm, AddCategoryForm
from main_app.models import Category


class IndexView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        result = super(IndexView, self).get_context_data(**kwargs)
        result.update({'time':timezone.now().time()})
        return result

class AddItemView(CreateView):
    form_class = AddItemForm
    success_url = reverse_lazy('time_line')
    template_name = 'add_item.html'

    def get_context_data(self, **kwargs):

        result = super(AddItemView, self).get_context_data(**kwargs)
        form = result['form']
        form.initial['category']="Select a"
        print form.initial
        result.update({'form':form})
        return result


class AddCategoryView(CreateView):
    template_name = 'edit_category.html'
    # model = Category
    form_class = AddCategoryForm
    success_url = reverse_lazy('add_category')


    def get_context_data(self, **kwargs):
        result = super(AddCategoryView, self).get_context_data(**kwargs)
        categories = Category.objects.all()
        result.update({'categories':categories})
        return result

class TimeLineView(TemplateView):
    template_name = 'home.html'

class CategoryDeleteView(FormView):
    template_name = 'edit_category.html'
    # model = Category
    form_class = AddCategoryForm
    success_url = reverse_lazy('add_category')

    def get(self, request, *args, **kwargs):
        print self.request.GET['category']





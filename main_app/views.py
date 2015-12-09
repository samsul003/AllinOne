import json
from django.contrib.auth.decorators import login_required
from django.core.mail import EmailMessage
from braces.views import LoginRequiredMixin
from django.core.urlresolvers import reverse_lazy, reverse
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.utils import timezone
from django.forms import forms
from django.shortcuts import render
# Create your views here.
from django.views.generic import TemplateView, ListView, CreateView, FormView, DeleteView
from AllInOne.settings import EMAIL_HOST_USER
from main_app.forms import AddItemForm, AddCategoryForm, AddCategoryAdminForm
from main_app.models import Category, Item, CategoryByUser
from datetime import timedelta


class IndexView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        result = super(IndexView, self).get_context_data(**kwargs)
        result.update({'time': timezone.now().time()})
        return result


class AddItemView(CreateView):
    form_class = AddItemForm
    success_url = reverse_lazy('time_line')
    template_name = 'add_item.html'

    def get_context_data(self, **kwargs):
        result = super(AddItemView, self).get_context_data(**kwargs)
        form = result['form']
        form.initial['category'] = "Select a"
        print form.initial
        result.update({'form': form})
        return result


class AddCategoryView(CreateView):
    template_name = 'edit_category.html'
    # model = Category
    form_class = AddCategoryForm
    success_url = reverse_lazy('add_category')

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_staff:
            return HttpResponseRedirect(reverse('add_category_admin'))
        else:
            return super(AddCategoryView, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        result = super(AddCategoryView, self).get_context_data(**kwargs)
        categories = CategoryByUser.objects.filter(user=self.request.user)
        result.update({'categories': categories})
        built_in_cats = Category.objects.all()
        result.update(({'built_in_cats': built_in_cats}))
        return result

    def form_valid(self, form):
        kwargs = {'user': self.request.user}
        obj = form.save(commit=False, **kwargs)
        return HttpResponseRedirect(self.success_url)


class AddCategoryViewAdmin(CreateView):
    template_name = 'add_category_admin.html'
    # model = Category
    form_class = AddCategoryAdminForm
    success_url = reverse_lazy('add_category_admin')

    def get_context_data(self, **kwargs):
        result = super(AddCategoryViewAdmin, self).get_context_data(**kwargs)
        categories = Category.objects.all()
        result.update({'categories': categories})
        return result

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_staff:
            return render(request, 'error.html', {
                "error": " You are not authorized to perform this"
                         " action. Please contact admin for further information."})
        else:
            return super(AddCategoryViewAdmin, self).dispatch(request, *args, **kwargs)


class TimeLineView(TemplateView):
    template_name = 'home.html'


class CategoryDeleteView(FormView):
    template_name = 'edit_category.html'
    # model = Category
    form_class = AddCategoryForm
    success_url = reverse_lazy('add_category')

    def get(self, request, *args, **kwargs):
        category = self.kwargs['category']
        category_obj = Category.objects.get(category_name=category)
        return super(CategoryDeleteView, self).get(self, request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        result = super(CategoryDeleteView, self).get_context_data(**kwargs)
        categories = Category.objects.all()
        result.update({'categories': categories})
        return result

    def form_valid(self, form):
        super(CategoryDeleteView, self).form_valid(form)
        form = self.get_form()


def delete_category(request):
    if request.method == 'POST':
        category = request.POST['category']
        response_data = {}
        category_obj = Category.objects.get(category_name=category)
        try:
            category_obj.delete()
            response_data['result'] = "Deleted "

        except:
            response_data['result'] = "Not Found"
        return HttpResponse(
            json.dumps(response_data),
            content_type="application/json"

        )


class Categories(LoginRequiredMixin, TemplateView):
    template_name = "add_category_admin.html"
    redirect_field_name = "next"

    # fields for LoginRequiredMixin
    login_url = reverse_lazy('login')


class CustomErrorView(TemplateView):
    template_name = "error.html"

    def get_context_data(self, **kwargs):
        param = self.request.GET.get("param", '')
        if param != '' and param == 'email_sent':
            error = " An e-mail has been sent to account. Please click on the link to verify your " \
                    "email account. No activity is possible until you verify."
            return {'error': error}
        else:
            return super(CustomErrorView, self).get_context_data(**kwargs)


# @login_required(login_url=reverse_lazy('login'))
class DashBoardView(TemplateView):
    template_name = 'dash_board.html'

    # def get_context_data(self, **kwargs):
    #     result = super(DashBoardView, self).get_context_data(**kwargs)
    #     today = timezone.now()
    #     data = {}
    #     last_week = today - timedelta(days=7)
    #     items_today = Item.objects.filter(user=self.request.user, purchase_date=timezone.now().date())
    #     items_this_week = Item.objects.filter(user=self.request.user, purchase_date__gte=last_week)
    #
    #     data['items_today'] = items_today
    #     data['items_this_week'] = items_this_week
    #     result.update({'items_today': items_today, 'items_this_week': items_this_week})
    #     return result

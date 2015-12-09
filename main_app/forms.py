from django import forms
from django.forms import ModelForm
from main_app.models import Item, Category, CategoryByUser
from django.utils.translation import ugettext_lazy as _


class AddItemForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(ModelForm, self).__init__(*args, **kwargs)
        self.css_class = "home_page"

    class Meta:
        model = Item
        fields = ['name', 'price', 'currency', 'category']
        help_texts = {
            'category': _('Some Text'),
        }


class AddCategoryForm(ModelForm):
    class Meta:
        model = CategoryByUser
        fields = ['category_name', 'description']
        widgets = {
            'category_name': forms.TextInput(
                attrs={'id': 'cat-name', 'required': True, 'placeholder': 'Name of The Category', 'size': '100'}
            ),
            'description': forms.Textarea(
                attrs={'required': False, 'placeholder': 'Describe which kind of items you are including','rows':3})
        }

    def save(self, commit=True, **kwargs):
        category = super(AddCategoryForm, self).save(commit=False)
        category.user = kwargs['user']
        category.save()
        # super(AddCategoryForm, self).save()


class AddCategoryAdminForm(ModelForm):
    class Meta:
        model = Category
        fields = ['category_name', 'description', ]
        widgets = {
            'category_name': forms.TextInput(
                attrs={'id': 'cat-name', 'required': True, 'placeholder': 'Name of The Category', 'size': '100'}
            ),
            'description': forms.Textarea(
                attrs={'required': False, 'placeholder': 'Describe which kind of items you are including','rows':3})
        }

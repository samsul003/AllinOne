from django import forms
from django.forms import ModelForm
from main_app.models import Item, Category
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
        model = Category
        fields = ['category_name','description']
        widgets = {
            'category_name': forms.TextInput(
                attrs={'id': 'cat-name', 'required': True, 'placeholder': 'Say something...','size':'100'}
            ),
        }

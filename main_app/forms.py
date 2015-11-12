from django.forms import ModelForm
from main_app.models import Item
from django.utils.translation import ugettext_lazy as _



class AddItemForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(ModelForm, self).__init__(*args, **kwargs)
        self.css_class = "home_page"

    class Meta:
        model = Item
        fields = ['name', 'price', 'currency', 'category']
        help_texts = {
            'category': _('Sop text.'),
        }


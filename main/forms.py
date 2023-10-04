from django.forms import ModelForm
from django import forms
from .models import Item


class DateInput(forms.DateInput):
    input_type = 'date'


class ItemForm(ModelForm):
    class Meta:
        model = Item
        fields = '__all__'
        exclude = ['user']

    def __init__(self, *args, **kwargs):
        super(ItemForm, self).__init__(*args, **kwargs)
        self.fields['image'].required = False

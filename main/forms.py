from django.forms import ModelForm
from django import forms
from .models import Item


class ItemForm(ModelForm):
    class Meta:
        model = Item
        fields = '__all__'
        # widgets = {
        #     'image': forms.FileInput(attrs={'class': 'form-control-file'})
        # }

    def __init__(self, *args, **kwargs):
        super(ItemForm, self).__init__(*args, **kwargs)
        self.fields['image'].required = False

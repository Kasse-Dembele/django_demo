from django import forms
from .models import Item
INPUTS_CLASS = "py-4 px-6 w-full rounded-xl border"

class AddItemForm(forms.ModelForm):

    class Meta:
        model = Item
        fields = ("category", "name", "description", "price", "image")
        widgets = {
            'category': forms.Select(attrs={
            'class': INPUTS_CLASS
            }),
            'name': forms.TextInput(attrs={
            'class': INPUTS_CLASS
            }),
            'description': forms.Textarea(attrs={
            'class': INPUTS_CLASS
            }),
            'price': forms.TextInput(attrs={
            'class': INPUTS_CLASS
            }),
            'image': forms.FileInput(attrs={
            'class': INPUTS_CLASS
            })
        }



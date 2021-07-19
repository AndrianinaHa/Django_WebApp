from django import forms
from .models import Employe
from django.utils.translation import gettext_lazy as _
from django.forms import ModelForm, Textarea, widgets


# DataFlair
class EmployeCreate(forms.ModelForm):
    class Meta:
        model = Employe
        fields = ['nom', 'prenom', 'dateN', 'adresse', 'contact', 'fonction', 'image']
        labels = {
            'nom': _('First Name'),
            'prenom': _('Last Name'),
            'dateN': _('Date of birth'),
            'adresse': _('Address'),
            'contact': _('Contact'),
            'fonction': _('Function'),
        }
        widgets = {
            'nom': forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': "e.g: John"}
            ),
            'prenom': forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': "e.g: Jayebird"}
            ),
            'dateN': forms.DateInput(
                attrs={'type': 'date', 'style': 'color:grey', 'class': 'form-control',
                       'placeholder': "e.g: 12/08/2001"}
            ),
            'adresse': forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': "Lot XV Alembert"}
            ),
            'contact': forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': "+261 34 11 207 28"}
            ),
            'fonction': forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': "Assistant worker"}
            ),
        }

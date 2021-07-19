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
            'dateN': _('Date de naissance'),
        }
        widgets = {
            'nom': forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': "le nom de l'employe"}
            ),
            'prenom': forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': "le prenom de l'employe"}
            ),
            'dateN': forms.DateInput(
                attrs={'type': 'date', 'style': 'color:grey', 'class': 'form-control',
                       'placeholder': "Date de naissance de l'employe"}
            ),
            'adresse': forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': "l'adresse de l'employe"}
            ),
            'contact': forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': "le contact de l'employe"}
            ),
            'fonction': forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': "la fonction l'employe"}
            ),
        }

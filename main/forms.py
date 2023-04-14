from django import forms
from main.models import Obavijest, Kolegij
from django.contrib.auth.models import User


class ObavijestForm(forms.ModelForm):
    class Meta:
        model = Obavijest
        fields = ["kolegij", "naziv", "opis", "datum_isteka"]
        widgets = {"datum_isteka": forms.DateInput(attrs={"type": "date"})}


class KolegijForm(forms.ModelForm):
    class Meta:
        model = Kolegij
        fields = ["predavaci", "naziv"]


class PredavacForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["first_name", "last_name", "email", "password"]

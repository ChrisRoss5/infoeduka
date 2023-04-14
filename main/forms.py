from django import forms
from main.models import Obavijest


class ObavijestForm(forms.ModelForm):
    class Meta:
        model = Obavijest
        fields = ["kolegij", "naziv", "opis", "datum_isteka"]
        widgets = {"datum_isteka": forms.DateInput(attrs={"type": "date"})}

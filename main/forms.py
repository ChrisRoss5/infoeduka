from django import forms
from main.models import Obavijest, Kolegij
from django.contrib.auth.models import User


class ObavijestForm(forms.ModelForm):
    class Meta:
        model = Obavijest
        fields = ["kolegij", "naziv", "opis", "datum_isteka"]
        widgets = {"datum_isteka": forms.DateInput(attrs={"type": "date"})}

    def __init__(self, user=None, *args, **kwargs):
        super(ObavijestForm, self).__init__(*args, **kwargs)

        if user and not user.is_staff:
            self.fields["kolegij"].queryset = self.fields["kolegij"].queryset.filter(
                predavaci__in=[user]
            )



class KolegijForm(forms.ModelForm):
    class Meta:
        model = Kolegij
        fields = ["predavaci", "naziv"]


class PredavacForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["first_name", "last_name", "email", "password"]

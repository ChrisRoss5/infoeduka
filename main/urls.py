from django.urls import path
from django.views.generic import RedirectView
from . import views

urlpatterns = [
    path("", RedirectView.as_view(url='obavijesti')),
    path("obavijesti", views.obavijesti, name="obavijesti"),
    path("obavijesti-nova", views.obavijesti_nova, name="obavijesti_nova"),
    path("obavijesti/obrisi/<int:id>", views.obrisi_obavijest, name="obrisi_obavijest"),
    path("obavijesti/uredi/<int:id>", views.uredi_obavijest, name="uredi_obavijest"),
    path("kolegij/unesi", views.kolegij_novi, name="kolegij_novi"),
    path("kolegij/obrisi/<int:id>", views.obrisi_kolegij, name="obrisi_kolegij"),
    path("kolegij/uredi/<int:id>", views.uredi_kolegij, name="uredi_kolegij"),
    path("kolegiji", views.kolegiji, name="kolegiji"),
    path("predavaci", views.predavaci, name="predavaci"),
    path("predavaci/unesi", views.predavaci_novi, name="predavaci_novi"),
    path("predavaci/obrisi/<int:id>", views.obrisi_predavaca, name="obrisi_predavaca"),
    path("predavaci/uredi/<int:id>", views.uredi_predavaca, name="uredi_predavaca"),
]

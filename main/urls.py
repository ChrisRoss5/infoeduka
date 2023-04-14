from django.urls import path, include
from django.views.generic import RedirectView
from . import views

urlpatterns = [
    path("", RedirectView.as_view(url='obavijesti')),
    path("obavijesti", views.obavijesti, name="obavijesti"),
    path("obavijesti-nova", views.obavijesti_nova, name="obavijesti_nova"),
    path("kolegiji", views.kolegiji, name="kolegiji"),
    path("predavaci", views.predavaci, name="predavaci"),
]

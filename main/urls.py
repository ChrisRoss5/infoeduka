from django.urls import path, include
from django.views.generic import RedirectView
from . import views

urlpatterns = [
    path("", RedirectView.as_view(url='kolegiji')),
    path("kolegiji", views.kolegiji, name="kolegiji"),
    path("predavaci", views.predavaci, name="predavaci"),
    path("obavijesti", views.obavijesti, name="obavijesti"),
]

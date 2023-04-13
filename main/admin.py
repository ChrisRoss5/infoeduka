from django.contrib import admin
from .models import Kolegij, Obavijest
from django.contrib.auth.models import Group

admin.site.unregister(Group)  # Nema potrebe za grupama
admin.site.register((Kolegij, Obavijest))

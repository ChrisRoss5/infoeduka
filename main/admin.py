from django.contrib import admin
from django.contrib.auth.models import Group
from .models import Kolegij, Obavijest


class ObavijestAdmin(admin.ModelAdmin):
    exclude = ("autor",)

    def save_model(self, request, obj, form, change):
        obj.autor = request.user
        obj.save()


admin.site.unregister(Group)  # Nema potrebe za grupama
admin.site.register(Kolegij)
admin.site.register(Obavijest, ObavijestAdmin)

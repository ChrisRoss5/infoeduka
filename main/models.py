from django.db import models
from django.contrib.auth.models import User

class Kolegij(models.Model):
    predavaci = models.ManyToManyField(User, limit_choices_to={"is_staff": False})
    naziv = models.CharField(max_length=100)

    def __str__(self):
        return self.naziv

    class Meta:
        verbose_name_plural = "Kolegiji"


class Obavijest(models.Model):
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    kolegij = models.ForeignKey(Kolegij, on_delete=models.CASCADE)
    naziv = models.CharField(max_length=100)
    opis = models.TextField()
    datum_objave = models.DateTimeField(auto_now_add=True)
    datum_isteka = models.DateTimeField()

    def __str__(self):
        return self.naziv

    class Meta:
        verbose_name_plural = "Obavijesti"

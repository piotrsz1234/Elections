from django.db import models

# Create your models here.

class Wybory(models.Model):
    nazwa = models.CharField(max_length=50)
    poczatekWyborow = models.DateTimeField()
    koniecWyborow = models.DateTimeField()
    maxKandydatow = models.IntegerField()


class Osoba(models.Model):
    imie = models.CharField(max_length=20)
    nazwisko = models.CharField(max_length=50)
    pesel = models.CharField(max_length=11)


class OsobaWybory(models.Model):
    wyboryId = models.ForeignKey(Wybory, on_delete=models.CASCADE)
    OsobaId = models.ForeignKey(Osoba, on_delete=models.CASCADE)
    czyOddalGlos = models.BooleanField(default=False)
    czyKandydat = models.BooleanField(default=False)


class Glos(models.Model):
    wyboryId = models.ForeignKey(Wybory, on_delete=models.CASCADE)
    kandydatOsobaID = models.ForeignKey(Osoba, on_delete=models.CASCADE)
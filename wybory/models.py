from django.db import models

# Create your models here.

class Wybory(models.Model):
    nazwa = models.CharField(max_length=50)
    poczatekWyborow = models.DateTimeField()
    koniecWyborow = models.DateTimeField()
    maxKandydatow = models.IntegerField()

    def __str__(self):
        return self.nazwa


class Osoba(models.Model):
    imie = models.CharField(max_length=20)
    nazwisko = models.CharField(max_length=50)
    pesel = models.CharField(max_length=11, unique=True)

    def __str__(self):
        return f'{self.imie} {self.nazwisko}'


class OsobaWybory(models.Model):
    wyboryId = models.ForeignKey(Wybory, on_delete=models.CASCADE)
    osobaId = models.ForeignKey(Osoba, on_delete=models.CASCADE)
    czyOddalGlos = models.BooleanField(default=False)
    czyKandydat = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.OsobaId.imie} {self.OsobaId.nazwisko} - {self.wyboryId.nazwa}'


class Glos(models.Model):
    wyboryId = models.ForeignKey(Wybory, on_delete=models.CASCADE)
    kandydatOsobaId = models.ForeignKey(Osoba, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.wyboryId.nazwa} - {self.kandydatOsobaID.imie} {self.kandydatOsobaID.nazwisko}'

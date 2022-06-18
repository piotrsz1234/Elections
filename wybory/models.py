from django.core.exceptions import ValidationError
from django.db import models

# Create your models here.

class Wybory(models.Model):
    nazwa = models.CharField(max_length=50)
    poczatekWyborow = models.DateTimeField()
    koniecWyborow = models.DateTimeField()
    maxWybranychKandydatow = models.IntegerField(default=1)

    def clean(self):
        if self.poczatekWyborow > self.koniecWyborow:
            raise ValidationError("Data początka wyborów musi być wcześniejsza niż data końca wyborów")
        if self.maxWybranychKandydatow < 1:
            raise ValidationError("Liczba kandydatów musi być większa od 0")


    def __str__(self):
        return self.nazwa


class Osoba(models.Model):
    imie = models.CharField(max_length=20)
    nazwisko = models.CharField(max_length=50)
    pesel = models.CharField(max_length=11, unique=True)

    def clean(self):
        if len(self.pesel) != 11 or not self.pesel.isnumeric():
            raise ValidationError("pesel musi składać się tylko z 11 cyfr")

    def __str__(self):
        return f'{self.imie} {self.nazwisko}'


class OsobaWybory(models.Model):
    wyboryId = models.ForeignKey(Wybory, on_delete=models.CASCADE)
    osobaId = models.ForeignKey(Osoba, on_delete=models.CASCADE)
    czyOddalGlos = models.BooleanField(default=False)
    czyKandydat = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.osobaId.imie} {self.osobaId.nazwisko} - {self.wyboryId.nazwa}'


class Glos(models.Model):
    wyboryId = models.ForeignKey(Wybory, on_delete=models.CASCADE)
    kandydatOsobaId = models.ForeignKey(Osoba, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.wyboryId.nazwa} - {self.kandydatOsobaID.imie} {self.kandydatOsobaID.nazwisko}'

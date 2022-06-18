from django.contrib import admin
from wybory.models import *

@admin.register(Osoba)
class OsobaAdmin(admin.ModelAdmin):
    list_display = ('imie', 'nazwisko', 'pesel')
    list_filter = ('imie','nazwisko')
    #readonly_fields = ('pesel',)
    search_fields = ('imie', 'nazwisko')
    ordering = ('imie', 'nazwisko', 'pesel')
    pass


@admin.register(OsobaWybory)
class OsobaWyboryAdmin(admin.ModelAdmin):
    list_display = ('wyboryId', 'osobaId', 'czyOddalGlos', 'czyKandydat')
    list_filter = ('wyboryId', 'osobaId', 'czyOddalGlos', 'czyKandydat')
    search_fields = ('wyboryId', 'osobaId')
    ordering = ('wyboryId', 'osobaId')
    pass

@admin.register(Wybory)
class WyboryAdmin(admin.ModelAdmin):
    list_display = ('nazwa', 'maxWybranychKandydatow', 'poczatekWyborow', 'koniecWyborow')
    list_filter = ('nazwa', 'poczatekWyborow', 'koniecWyborow')
    search_fields = ('nazwa', 'poczatekWyborow', 'koniecWyborow')
    ordering = ('poczatekWyborow', 'koniecWyborow', 'nazwa', 'maxWybranychKandydatow')
    pass

@admin.register(Glos)
class GlosAdmin(admin.ModelAdmin):
    list_display = ('wyboryId', 'kandydatOsobaId')
    list_filter = ('wyboryId', 'kandydatOsobaId')
    search_fields = ('wyboryId', 'kandydatOsobaId')
    ordering = ('wyboryId', 'kandydatOsobaId')
    pass


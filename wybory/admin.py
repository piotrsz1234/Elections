from django.contrib import admin

# Register your models here.
from wybory.models import *

admin.site.register(Osoba)
admin.site.register(OsobaWybory)
admin.site.register(Wybory)
admin.site.register(Glos)

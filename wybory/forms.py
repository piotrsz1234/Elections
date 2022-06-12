from django import forms
from django.core.exceptions import ValidationError

from .models import Osoba


class VoteForm(forms.Form):

    def __init__(self, candidates, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['kandydaci'] = forms.ChoiceField(choices=candidates, widget=forms.RadioSelect)
    kandydaci = forms.ChoiceField()


class LoginForm(forms.Form):
    imie = forms.CharField(max_length=20)
    nazwisko = forms.CharField(max_length=50)
    pesel = forms.CharField(max_length=11)

    def clean_pesel(self):
        pesel = self.cleaned_data['pesel']

        if len(pesel) != 11:
            raise ValidationError("Pesel musi mieć długość 11 cyfr")
        if not pesel.isnumeric():
            raise ValidationError("Pesel musi składać się tylko z cyfr")

        return pesel


    def clean(self):
        cleaned_data = super().clean()
        pesel = cleaned_data.get('pesel')
        imie = cleaned_data.get('imie')
        nazwisko = cleaned_data.get('nazwisko')

        if pesel and imie and nazwisko:
            osoba = Osoba.objects.filter(pesel=pesel)
            if not osoba:
                raise ValidationError("Nie ma takiej osoby")
            elif osoba[0].imie != imie or osoba[0].nazwisko != nazwisko:
                raise ValidationError("Nie ma takiej osoby")


    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
        self.fields['pesel'].widget.attrs['class'] = 'form-control form-control-sm'
        self.fields['imie'].widget.attrs['class'] = 'form-control form-control-sm'
        self.fields['nazwisko'].widget.attrs['class'] = 'form-control form-control-sm'

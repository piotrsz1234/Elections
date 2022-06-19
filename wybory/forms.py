from django import forms

from .models import Osoba


class VoteForm(forms.Form):
    kandydaci = forms.ChoiceField()

    def __init__(self, candidates, election, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['kandydaci'] = forms.MultipleChoiceField(choices=candidates, widget=forms.CheckboxSelectMultiple)
        self.election = election

    def clean_kandydaci(self):
        candidates = self.cleaned_data['kandydaci']
        if len(candidates) > self.election.maxWybranychKandydatow:
            raise forms.ValidationError(f"możesz zagłosować na max {self.election.maxWybranychKandydatow} kandydatów")
        return candidates



class LoginForm(forms.Form):
    imie = forms.CharField(max_length=20)
    nazwisko = forms.CharField(max_length=50)
    pesel = forms.CharField(max_length=11)

    def clean_pesel(self):
        pesel = self.cleaned_data['pesel']

        if len(pesel) != 11:
            raise forms.ValidationError("Pesel musi mieć długość 11 cyfr")
        if not pesel.isnumeric():
            raise forms.ValidationError("Pesel musi składać się tylko z cyfr")

        return pesel


    def clean(self):
        cleaned_data = super().clean()
        pesel = cleaned_data.get('pesel')
        imie = cleaned_data.get('imie')
        nazwisko = cleaned_data.get('nazwisko')

        if pesel and imie and nazwisko:
            osoba = Osoba.objects.filter(pesel=pesel)
            if not osoba:
                raise forms.ValidationError("Nie ma takiej osoby")
            elif osoba[0].imie != imie or osoba[0].nazwisko != nazwisko:
                raise forms.ValidationError("Nie ma takiej osoby")


    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
        self.fields['pesel'].widget.attrs['class'] = 'form-control form-control-sm'
        self.fields['imie'].widget.attrs['class'] = 'form-control form-control-sm'
        self.fields['nazwisko'].widget.attrs['class'] = 'form-control form-control-sm'

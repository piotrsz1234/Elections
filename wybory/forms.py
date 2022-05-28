from django import forms


class VoteForm(forms.Form):

    def __init__(self, candidates, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['kandydaci'] = forms.ChoiceField(choices=candidates, widget=forms.RadioSelect)


    kandydaci = forms.ChoiceField()

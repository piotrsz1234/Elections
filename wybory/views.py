from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.template import loader

from wybory.models import *
from .forms import VoteForm


def renderView(request, viewName, arguments):
    layout = loader.get_template('base.html')
    template = loader.get_template(viewName)
    return layout.render({'body': template.render(arguments, request)}, request)


def index(request):
    if request.session.has_key('UserID') is False:
        return redirect('login')
    user = Osoba.objects.filter(pesel=request.session['UserID'])[0]
    elections = OsobaWybory.objects.order_by('wyboryId_id').filter(OsobaId_id=user.pk)[:10]
    return render(request, "index.html", {'user': user, 'elections': elections})


def login(request):
    if request.session.has_key('UserID') is True:
        return redirect('index')
    return render(request, 'login.html', {})


def loginUser(request):
    if len(request.POST['pesel']) != 11:
        return redirect('login')
    users = Osoba.objects.filter(pesel=request.POST['pesel']).filter(imie=request.POST['firstName']).filter(
        nazwisko=request.POST['lastName'])
    if len(users) == 0:
        return redirect('login')
    request.session['UserID'] = users[0].pesel

    return redirect('index')


def vote(request, election_id):
    # TODO sprawdzic czy kandydat glosowal i czy uprawniony
    kandydaci_wybory = OsobaWybory.objects.filter(wyboryId__exact=election_id).filter(czyKandydat__exact=True)
    kandydaci = [(k.OsobaId.id, f'{k.OsobaId.imie} {k.OsobaId.nazwisko}') for k in kandydaci_wybory]
    election = Wybory.objects.get(pk=election_id)

    if request.method == 'POST':
        form = VoteForm(kandydaci, request.POST)
        if form.is_valid():
            glos = Glos(wyboryId_id=election_id, kandydatOsobaID_id=form.cleaned_data['kandydaci'])
            glos.save()
            return HttpResponse("WYGRAL ANDRZEJ DUDA")
    else:
        form = VoteForm(kandydaci)

    return render(request, 'wybory/vote.html', {'form': form, 'election': election})


def electionResults(request, election_id):
    election = Wybory.objects.filter(pk=election_id)[0]
    possibleVoteCount = OsobaWybory.objects.filter(wyboryId_id=election_id).filter(czyKandydat=False).count()
    voteCount = OsobaWybory.objects.filter(wyboryId_id=election_id).filter(czyOddalGlos=True).count()
    return HttpResponse(renderView(request, 'electionResults.html', {
        'election': election,
        'possibleVoteCount': possibleVoteCount,
        'totalVoteCount': voteCount
    }))

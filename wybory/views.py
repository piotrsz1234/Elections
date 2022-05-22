from django.http import HttpResponse
from django.shortcuts import redirect
from django.template import loader

from wybory.models import *


def renderView(request, viewName, arguments):
    layout = loader.get_template('base.html')
    template = loader.get_template(viewName)
    return layout.render({'body': template.render(arguments, request)}, request)


def index(request):
    if request.session.has_key('UserID') is False:
        return redirect('login')
    user = Osoba.objects.filter(pesel=request.session['UserID'])[0]
    elections = OsobaWybory.objects.order_by('wyboryId_id').filter(OsobaId_id=user.pk)[:10]
    return HttpResponse(renderView(request, "index.html", {'user': user, 'elections': elections}))


def login(request):
    if request.session.has_key('UserID') is True:
        return redirect('index')
    return HttpResponse(renderView(request, 'login.html', {}))


def loginUser(request):
    if len(request.POST['pesel']) != 11:
        return redirect('login')
    users = Osoba.objects.filter(pesel=request.POST['pesel']).filter(imie=request.POST['firstName']).filter(nazwisko=request.POST['lastName'])
    if len(users) == 0:
        return redirect('login')
    request.session['UserID'] = users[0].pesel
    
    return redirect('index')
    

def vote(request, electionId):
    list = OsobaWybory.objects.filter(wyboryId_id=electionId).filter(czyKandydat=True)
    return HttpResponse(renderView(request, 'vote.html', {'candidate_list': list}))


def electionResults(request, electionId):
    election = Wybory.objects.filter(pk=electionId)[0]
    possibleVoteCount = OsobaWybory.objects.filter(wyboryId_id=electionId).filter(czyKandydat=False).count()
    voteCount = OsobaWybory.objects.filter(wyboryId_id=electionId).filter(czyOddalGlos=True).count()
    return HttpResponse(renderView(request, 'electionResults.html', {
        'election': election,
        'possibleVoteCount': possibleVoteCount,
        'totalVoteCount': voteCount
    }))
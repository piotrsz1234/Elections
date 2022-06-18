from django.http import HttpResponse
from django.shortcuts import render, redirect
from wybory.models import *
from .forms import VoteForm
from .decorator import login_required
from django.utils import timezone
from .dtos import ElectionDto


@login_required
def index(request):
    user = Osoba.objects.filter(pesel=request.session['UserID'])[0]
    elections = OsobaWybory.objects.order_by('wyboryId_id').filter(osobaId_id=user.pk)[:10]
    electionsDtos = []
    for e in elections:
        electionsDtos.append(ElectionDto(e.wyboryId_id, e.wyboryId.nazwa,e.wyboryId.poczatekWyborow.strftime("%m/%d/%Y %H:%M"),e.wyboryId.koniecWyborow.strftime("%m/%d/%Y %H:%M")))

    return render(request, "index.html", {'user': user, 'elections': electionsDtos})


@login_required
def vote(request, election_id):
    election = Wybory.objects.get(pk=election_id)
    if timezone.now() < election.poczatekWyborow or election.koniecWyborow < timezone.now():
        return HttpResponse("To nie czas na glosowanie")

    # wszystkie osoby zwiazane z konkretnymi wyborami
    elections_people = OsobaWybory.objects.filter(wyboryId_id=election_id)

    # użytkownik
    user = elections_people.filter(osobaId__pesel=request.session['UserID'])

    # jeśli użytkownika nie ma w wborach
    if not user:
        return HttpResponse("Nie masz prawa glosować w tych wyborach")

    if user[0].czyOddalGlos:
        return HttpResponse("Już zaglosowaleś w tych wyborach")

    candidates_in_elections = elections_people.filter(czyKandydat__exact=True)

    # krotka z id kandydata i jego nazwa do formularza glosowania
    candidates = [(k.OsobaId.id, f'{k.OsobaId.imie} {k.OsobaId.nazwisko}') for k in candidates_in_elections]

    if request.method == 'POST':
        form = VoteForm(candidates, request.POST)
        if form.is_valid():
            kandydaci = form.cleaned_data['kandydaci']
            if len(kandydaci) < 1 or len(kandydaci) > election.maxWybranychKandydatow:
                return HttpResponse(f"możesz zagłosować na max {election.maxWybranychKandydatow} kandydatów")
            # utworzenie glosu i go zapisanie w bazei
            for kandydat in kandydaci:
                glos = Glos(wyboryId_id=election_id, kandydatOsobaID_id=kandydat)
                glos.save()

            # oznaczenie ze urzytkownik oddal glos i zapisanie w bazie
            user[0].czyOddalGlos = True
            user[0].save()
            return redirect('index')
    else:
        form = VoteForm(candidates)

    return render(request, 'vote.html', {'form': form, 'election': election})


def election_results(request, election_id):
    election = Wybory.objects.get(pk=election_id)

    if election.koniecWyborow > timezone.now():
        return HttpResponse("Wybory sie jeszcze nie skonczyly")

    # liczba wszystkich glosow
    total_vote_count = Glos.objects.filter(wyboryId=election_id).count()

    #kandydaci
    candidates = OsobaWybory.objects.filter(wyboryId_id=election_id).filter(czyKandydat__exact=True)

    # lista slownikow z nazwa kanydata liczba glosow i procentem glosow
    candidates_and_votes = []
    for candidat in candidates:
        # liczba glosow na kandydata
        candidate_total_vote = Glos.objects.filter(wyboryId=election_id).filter(kandydatOsobaID=candidat.OsobaId).count()
        percent =  round(candidate_total_vote / total_vote_count * 100, 2) if total_vote_count > 0 else 0
        candidates_and_votes.append({
            'name': f'{candidat.OsobaId.imie} {candidat.OsobaId.nazwisko}',
            'count': candidate_total_vote,
            'percent': percent
        })

    return render(request, 'electionResults.html', {
        'election': election,
        'candidates_vote_count': candidates_and_votes,
        'total_vote_count': total_vote_count
    })

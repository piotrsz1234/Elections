from django.http import HttpResponse
from django.shortcuts import redirect
from django.template import loader

from wybory.models import OsobaWybory


def renderView(request, viewName, arguments):
    layout = loader.get_template('base.html')
    template = loader.get_template(viewName)
    return layout.render({'body': template.render(arguments, request)}, request)


def index(request):
    return HttpResponse(renderView(request, "index.html", {}))


def login(request):
    return HttpResponse(renderView(request, 'login.html', {}))


def loginUser(request):
    if len(request.POST['pesel']) != 11:
        return redirect('login')


def vote(request):
    list = OsobaWybory.objects.order_by('OsobaId')[:100]
    return HttpResponse(renderView(request, 'vote.html', { 'candidate_list': list }))

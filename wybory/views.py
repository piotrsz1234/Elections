from django.http import HttpResponse
from django.template import loader


def renderView(request, viewName):
    layout = loader.get_template('base.html')
    template = loader.get_template(viewName)
    return layout.render({'body': template.render({}, request)}, request)


def index(request):
    return HttpResponse(renderView(request, "index.html"))

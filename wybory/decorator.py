from django.http import HttpResponseRedirect


def login_required(function):
    def wrapper(request, *args, **kw):
        if not (request.session.get('UserID')):
            return HttpResponseRedirect('/login/')
        else:
            return function(request, *args, **kw)

    wrapper.__doc__ = function.__doc__
    wrapper.__name__ = function.__name__
    return wrapper
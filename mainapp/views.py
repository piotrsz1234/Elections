from django.shortcuts import redirect, render
from wybory.forms import LoginForm
from wybory.decorator import login_required

def login(request):
    if request.session.has_key('UserID') is True:
        return redirect('index')

    if request.method == 'POST':
        form = LoginForm(request.POST)

        if form.is_valid():
            request.session['UserID'] = form.cleaned_data['pesel']
            return redirect('index')

    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})


@login_required
def logout(request):
    del request.session['UserID']
    return redirect('index')

def home(request):
    return render(request, 'home.html', {})
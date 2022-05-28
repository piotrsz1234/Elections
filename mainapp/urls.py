from django.urls import path, include
from django.contrib import admin
from django.views.generic import RedirectView
from wybory.views import login, loginUser

urlpatterns = [
    path('admin/', admin.site.urls),
    path('wybory/', include('wybory.urls')),
    path('', RedirectView.as_view(url='wybory/', permanent=True)),
    path('login', login, name='login'),
    path('loginUser', loginUser, name='loginUser'),
]
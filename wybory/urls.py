from django.template.defaulttags import url
from django.urls import path
from django.contrib import admin

from . import views

urlpatterns = [
    path('admin', admin.site.urls),
    path('', views.index, name='index'),
    path('login', views.login, name='login'),
    path('loginUser', views.loginUser, name='loginUser'),
    path('vote/<electionId>', views.vote, name='vote'),
    path('electionResults/<electionId>', views.electionResults, name='electionResults'),
]
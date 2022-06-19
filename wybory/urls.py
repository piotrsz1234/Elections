from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('vote/<int:election_id>', views.vote, name='vote'),
    path('electionResults/<int:election_id>', views.election_results, name='electionResults'),
    path('pdf/<int:election_id>', views.generatePdf, name='pdf')
]
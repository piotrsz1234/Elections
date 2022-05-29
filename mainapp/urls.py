from django.urls import path, include
from django.contrib import admin
from .views import login, logout, home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('wybory/', include('wybory.urls')),
    path('', home, name='home'),
    path('login/', login, name='login'),
    path('logout/', logout, name='logout'),
]
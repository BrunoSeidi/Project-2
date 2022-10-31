from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    
]+staticfiles_urlpatterns()
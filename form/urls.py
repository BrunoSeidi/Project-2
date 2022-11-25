from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path
from . import views
from form.views import create_extra


urlpatterns = [
    path('', views.home, name='home'),
    path('htmx/extra/', create_extra, name='create-extra'),
    
]+staticfiles_urlpatterns()
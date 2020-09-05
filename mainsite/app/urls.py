from django.urls import path
from . import views

# importing dash app to pre-render
from django.views.generic import RedirectView

urlpatterns = [
    path('gettopgains', views.gettopgains, name='gettopgains'),
    path('getnews', views.getnews, name='getnews'),
    path('getcompanysymbol', views.getcompanysymbol, name='getcompanysymbol'),
    path('getcompanydata', views.getcompanydata, name='getcompanydata'),
]
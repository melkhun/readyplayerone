from django.urls import path
from . import views

# importing dash app to pre-render
from django.views.generic import RedirectView

urlpatterns = [
    path('gettopgains', views.gettopgains, name='gettopgains'),
    path('getTopETFs', views.getTopETFs, name='getTopETFs'),
    path('getFutures', views.getFutures, name='getFutures'),
    path('getBonds', views.getBonds, name='getBonds'),
    path('getOptions', views.getOptions, name='getOptions'),
    # path('getForex', views.getForex, name='getForex'),
    path('getnews', views.getnews, name='getnews'),
    path('getcompanysymbol', views.getcompanysymbol, name='getcompanysymbol'),
    path('getcompanydata', views.getcompanydata, name='getcompanydata'),
]
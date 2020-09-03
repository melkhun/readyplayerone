from django.urls import path
from . import views

# importing dash app to pre-render
from .dash_apps.finished_apps import sample_dash_app

# index path
urlpatterns = [
    path('', views.index, name='index'),
]

# sidebar paths
urlpatterns += [
    path('maindashboard', views.maindashboard, name='maindashboard'),
    path('financialcalculators', views.financialcalculators, name='financialcalculators')
]

# calculator paths
urlpatterns += [
    path('financialcalculators/budget', views.budgetcalculator, name='budgetcalculator'),
    path('financialcalculators/networth', views.networthcalculator, name='networthcalculator'),
]
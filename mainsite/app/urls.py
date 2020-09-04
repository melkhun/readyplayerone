from django.urls import path
from . import views

# importing dash app to pre-render
from .dash_apps.finished_apps import sample_dash_app

# index path
urlpatterns = [
    path('', views.index, name='index'),
]

# account paths
urlpatterns += [
    path('login', views.loginPage, name='login'),
    path('logout', views.logoutUser, name='logout'),
    path('register', views.register, name='register'),
    path('profile', views.profile, name='profile'),
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

urlpatterns += [
    path('quickstart', views.quickstart, name='quickstart'),
]
from django.urls import path
from . import views

# importing dash app to pre-render
from .dash_apps.finished_apps import sample_dash_app
from .dash_apps.finished_apps import prices_app
from django.views.generic import RedirectView

# index path
urlpatterns = [
    path('', RedirectView.as_view(url='index.html')),
    path('index.html', views.index, name='index'),
]

# account paths
urlpatterns += [
    path('login', views.loginPage, name='login'),
    path('logout', views.logoutUser, name='logout'),
    path('register', views.register, name='register'),
]

# sidebar paths
urlpatterns += [
    path('maindashboard', views.maindashboard, name='maindashboard'),
    path('testdashboard', views.testdashboard, name='testdashboard'),
    # path('financialcalculators', views.financialcalculators, name='financialcalculators')
]

# calculator paths
# urlpatterns += [
#     path('financialcalculators/budget', views.budgetcalculator, name='budgetcalculator'),
#     path('financialcalculators/networth', views.networthcalculator, name='networthcalculator'),
# ]

urlpatterns += [
    path('quickstart', views.quickstart, name='quickstart'),
]

urlpatterns += [
    path('gettopgains', views.gettopgains, name='gettopgains'),
    path('getnews', views.getnews, name='getnews'),
]
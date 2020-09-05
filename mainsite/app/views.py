from django.shortcuts import render
from plotly.offline import plot
import plotly.graph_objects as go

from django.contrib.auth.decorators import login_required

# Create your views here.

# api views
from django.http import JsonResponse
from .scrape import *
def gettopgains(request):
    response_data = {}
    print(get_top_gains())
    return JsonResponse(get_top_gains().to_dict())

import urllib.request, json 
from .api_key import *
def getnews(request):
    with urllib.request.urlopen("https://newsapi.org/v2/top-headlines?country=sg&category=business&apiKey=" + NEWS_API) as url:
        data = json.loads(url.read().decode())
    return JsonResponse(data)


def getcompanysymbol(request):
    if request.method == "GET":
        keyword = request.GET.get("keyword")
        with urllib.request.urlopen("https://www.alphavantage.co/query?function=SYMBOL_SEARCH&keywords="+ keyword +"&apikey=" + ALPHA_VANTAGE_API) as url:
            data = json.loads(url.read().decode())
    else:
        data = {}
    return JsonResponse(data)

def getcompanydata(request):
    if request.method == "GET":
        symbol = request.GET.get("symbol")
        with urllib.request.urlopen("https://www.alphavantage.co/query?function=OVERVIEW&symbol="+ symbol +"&apikey=" + ALPHA_VANTAGE_API) as url:
            data = json.loads(url.read().decode())
    else:
        data = {}
    return JsonResponse(data)
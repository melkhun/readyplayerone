from django.shortcuts import render
from plotly.offline import plot
import plotly.graph_objects as go

from django.contrib.auth.decorators import login_required

# Create your views here.

from django.http import JsonResponse
from .scrape import *

def gettopgains(request):
    response_data = {}
    resp = JsonResponse(get_top_gains().to_dict())
    resp["Access-Control-Allow-Origin"] = "*"
    return resp


def getTopETFs(request):
    response_data = {}
    resp = JsonResponse(get_top_etfs().to_dict())
    resp["Access-Control-Allow-Origin"] = "*"
    return resp


def getFutures(request):
    response_data = {}
    resp = JsonResponse(get_futures().to_dict())
    resp["Access-Control-Allow-Origin"] = "*"
    return resp


def getBonds(request):
    response_data = {}
    resp = JsonResponse(get_bonds().to_dict())
    resp["Access-Control-Allow-Origin"] = "*"
    return resp


def getOptions(request):
    response_data = {}
    resp = JsonResponse(get_options().to_dict())
    resp["Access-Control-Allow-Origin"] = "*"
    return resp


# API gives error but tbh the data doesnt need formatting
# def getForex(request):
#     api = "https://eservices.mas.gov.sg/api/action/datastore/search.json?resource_id=95932927-c8bc-4e7a-b484-68a66a24edfe&limit=5&sort=end_of_day desc"

#     with urllib.request.urlopen(api) as url:
#         data = json.loads(url.read().decode())
#     resp = JsonResponse(data)
#     resp["Access-Control-Allow-Origin"] = "*"
#     return resp


import urllib.request, json 
from .api_key import *
def getnews(request):
    with urllib.request.urlopen("https://newsapi.org/v2/top-headlines?country=sg&category=business&apiKey=" + NEWS_API) as url:
        data = json.loads(url.read().decode())
    resp = JsonResponse(data)
    resp["Access-Control-Allow-Origin"] = "*"
    return resp


def getcompanysymbol(request):
    if request.method == "GET":
        keyword = request.GET.get("keyword")
        with urllib.request.urlopen("https://www.alphavantage.co/query?function=SYMBOL_SEARCH&keywords="+ keyword +"&apikey=" + ALPHA_VANTAGE_API) as url:
            data = json.loads(url.read().decode())
    else:
        data = {}
    resp = JsonResponse(data)
    resp["Access-Control-Allow-Origin"] = "*"
    return resp

def getcompanydata(request):
    if request.method == "GET":
        symbol = request.GET.get("symbol")
        with urllib.request.urlopen("https://www.alphavantage.co/query?function=OVERVIEW&symbol="+ symbol +"&apikey=" + ALPHA_VANTAGE_API) as url:
            data = json.loads(url.read().decode())
    else:
        data = {}
    resp = JsonResponse(data)
    resp["Access-Control-Allow-Origin"] = "*"
    return resp

def testend(request):
    if request.method == "GET":
        ticker = request.GET.get("ticker")

def getselectedquickstart(request):
    if request.method == "GET":
        symbol = request.GET.get("symbol")
        data = {"status": "success"}
    else:
        data = {"status":"error"}
    resp = JsonResponse(data)
    resp["Access-Control-Allow-Origin"] = "*"
    return resp

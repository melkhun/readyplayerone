from django.shortcuts import render
from plotly.offline import plot
import plotly.graph_objects as go

from django.forms.models import model_to_dict
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

from .models import Portfolio

def addSelectedPortfolio(request):
    if request.method == "GET":
        category = request.GET.get("category")
        symbol = request.GET.get("symbol")
        username = request.GET.get("username")

        try:
            existingRow = Portfolio.objects.get(username=username, category=category, symbol=symbol)
            data = {"status":"existing data, not added"}
        
        except:
            portfolio_instance = Portfolio(username=username, category=category, symbol=symbol)
            portfolio_instance.save()
            data = {"status": "success"}

    resp = JsonResponse(data)
    resp["Access-Control-Allow-Origin"] = "*"
    return resp

def deleteportfolioasset(request):
    if request.method == "GET":
        category = request.GET.get("category")
        symbol = request.GET.get("symbol")
        username = request.GET.get("username")

        print('deleteing for', category, symbol)

        try:
            portfolio_instance = Portfolio.objects.get(username=username, symbol=symbol, category=category)
            portfolio_instance.delete()

            data = {"status": "success"}
        except:
            data = {"status":"error"}
    else:
        data = {"status":"error"}
    resp = JsonResponse(data)
    resp["Access-Control-Allow-Origin"] = "*"
    return resp


def getUserPortfolio(request):
    if request.method == "GET":
        username = request.GET.get("username")
        results = {}

        try:
            allPortfolio = Portfolio.objects.filter(username=username)
            for eachRow in allPortfolio:
                eachRowDict = model_to_dict(eachRow)
                results[eachRowDict['symbol']] = eachRowDict['category']
            data = {
                "status": "success",
                "portfolio": results
            }
        except:
            data = {"status":"user does not exist, or portfolio is empty"}

        resp = JsonResponse(data)
        resp["Access-Control-Allow-Origin"] = "*"
        return resp
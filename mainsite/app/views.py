from django.shortcuts import render
from plotly.offline import plot
import plotly.graph_objects as go

from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required(login_url='login')
def index(request):
    return render(request, 'index.html')

@login_required(login_url='login')
def maindashboard(request):
    def scatter():
        x1 = [1,2,3,4]
        y1 = [30, 35, 25, 45]

        trace = go.Scatter(
            x=x1,
            y=y1,
        )
        layout = dict(
            title='Simple Graph',
            xaxis=dict(range=[min(x1), max(x1)]),
            yaxis=dict(range=[min(y1), max(y1)]),
        )
        fig = go.Figure(data=[trace], layout=layout)
        plot_div = plot(fig, output_type='div', include_plotlyjs=False)
        return plot_div

    context = {
        'plot': scatter()
    }

    return render(request, 'app/main_dashboard.html', context)



@login_required(login_url='login')
def testdashboard(request):
    context = {}
    return render(request, 'app/test_dashboard.html', context)

from django.http import JsonResponse
from .scrape import *
def gettopgains(request):
    response_data = {}
    # print(get_top_gains())
    resp = JsonResponse(get_top_gains().to_dict())
    resp["Access-Control-Allow-Origin"] = "*"
    return resp

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

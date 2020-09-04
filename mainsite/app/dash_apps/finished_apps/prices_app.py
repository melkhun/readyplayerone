# source: https://github.com/plotly/dash-stock-tickers-demo-app/blob/master/app.py
import dash
import dash_core_components as dcc
import dash_html_components as html
from django_plotly_dash import DjangoDash
from yahoo_fin import stock_info
from datetime import date, timedelta
import requests

import colorlover as cl
import datetime as dt
import flask
import os
import pandas as pd
import time

API_URL = 'https://www.alphavantage.co/query'
API_KEY = '1AQJR11NN012I7XO'

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = DjangoDash('TestGraph', external_stylesheets=external_stylesheets)

colorscale = cl.scales['9']['qual']['Paired']


# for sameple bc i lazy find actual list and read from it for now
listOfTickers = stock_info.tickers_dow()

# topGainers = stock_info.get_day_gainers()
# print(topGainers)

app.layout = html.Div([
    html.Div([
        html.H2('Finance Explorer',
                style={'display': 'inline',
                       'float': 'left',
                       'font-size': '2.65em',
                       'margin-left': '7px',
                       'font-weight': 'bolder',
                       'font-family': 'Product Sans',
                       'color': "rgba(117, 117, 117, 0.95)",
                       'margin-top': '20px',
                       'margin-bottom': '0'
                       }),
    ]),
    dcc.Dropdown(
        id='stock-ticker-input',
        options=[{'label': listOfTickers[i], 'value': listOfTickers[i]}
                 for i in range(len(listOfTickers))],
        value=['MSFT', 'AAPL'],
        multi=True
    ),
    html.Div(id='graphs')
], className="container")

def bbands(price, window_size=10, num_of_std=5):
    rolling_mean = price.rolling(window=window_size).mean()
    rolling_std  = price.rolling(window=window_size).std()
    upper_band = rolling_mean + (rolling_std*num_of_std)
    lower_band = rolling_mean - (rolling_std*num_of_std)
    return rolling_mean, upper_band, lower_band

@app.callback(
    dash.dependencies.Output('graphs','children'),
    [dash.dependencies.Input('stock-ticker-input', 'value')])

def update_graph(tickers):
    graphs = []

    if not tickers:
        graphs.append(html.H3(
            "Select a stock ticker.",
            style={'marginTop': 20, 'marginBottom': 20}
        ))
    else:
        enddate = date.today()

        allDates = pd.date_range(start='07/01/2020', end=enddate, closed=None)
        allDates.format(formatter=lambda x: x.strftime('%m/%d/%Y'))
        
        for i, ticker in enumerate(tickers):
            dff = {}
            dff = stock_info.get_data(ticker, start_date='01/01/2020', end_date=enddate)

            # req_data = { "function": "TIME_SERIES_DAILY", 
            #             "symbol": ticker,
            #             "apikey": API_KEY } 
            # api_response = requests.get(API_URL, req_data) 
            # data = api_response.json()
            # print(data)

            candlestick = {
                'x': allDates,
                'open': dff['open'],
                'high': dff['high'],
                'low': dff['low'],
                'close': dff['close'],
                'type': 'candlestick',
                'name': ticker,
                'legendgroup': ticker,
                'increasing': {'line': {'color': colorscale[0]}},
                'decreasing': {'line': {'color': colorscale[1]}}
            }
            bb_bands = bbands(dff.close)
            bollinger_traces = [{
                'x': allDates, 'y': y,
                'type': 'scatter', 'mode': 'lines',
                'line': {'width': 1, 'color': colorscale[(i*2) % len(colorscale)]},
                'hoverinfo': 'none',
                'legendgroup': ticker,
                'showlegend': True if i == 0 else False,
                'name': '{} - bollinger bands'.format(ticker)
            } for i, y in enumerate(bb_bands)]
            graphs.append(dcc.Graph(
                id=ticker,
                figure={
                    'data': [candlestick] + bollinger_traces,
                    'layout': {
                        'margin': {'b': 0, 'r': 10, 'l': 60, 't': 0},
                        'legend': {'x': 0}
                    }
                }
            ))



    return graphs


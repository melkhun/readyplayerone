from django.shortcuts import render
from plotly.offline import plot
import plotly.graph_objects as go

# Create your views here.
def index(request):
    return render(request, 'index.html')

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

def financialcalculators(request):
    return render(request, 'app/calculators/overview.html')

def budgetcalculator(request):
    income = 0
    expense = 0
    cashflow = 0
    if request.method == "POST":
        income = request.POST['income']
        expense = request.POST['expense']
        cashflow = float(income)-float(expense)
    context = {
        'income': income,
        'expense': expense,
        'cashflow': cashflow,
    }
    return render(request, 'app/calculators/budget_calculator.html', context)
    
def networthcalculator(request):
    assets = 0
    liabilities = 0
    networth = 0
    if request.method == "POST":
        assets = request.POST['assets']
        liabilities = request.POST['liabilities']
        networth = float(assets)-float(liabilities)
    context = {
        'assets': assets,
        'liabilities': liabilities,
        'networth': networth,
    }
    return render(request, 'app/calculators/networth_calculator.html', context)
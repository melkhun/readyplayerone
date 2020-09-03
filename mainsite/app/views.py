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


# accounts views
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

def loginPage(request):
    if request.user.is_authenticated:
        return redirect('index')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('index')
            else:
                messages.error(request, 'Username or password is incorrect')
    context = {}
    return render(request, 'app/accounts/login.html', context)

def logoutUser(request):
    logout(request)
    return redirect('login')

def register(request):
    if request.user.is_authenticated:
        return redirect('index')
    form = UserCreationForm()
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account successfully created')
            return redirect('login')
    context = {
        'form': form
        }
    return render(request, 'app/accounts/register.html', context)

# calculator views
@login_required(login_url='login')
def financialcalculators(request):
    return render(request, 'app/calculators/overview.html')

@login_required(login_url='login')
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
    
@login_required(login_url='login')
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
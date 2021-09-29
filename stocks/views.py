from django.shortcuts import render
import requests
from .models import Stock
from .forms import StockForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

stock_api_key = 'UFWJ7MO87LLQIV5F'

def get_stock(stock_id):
    return Stock.objects.get(id=stock_id)

def get_stock_detail(request, stock_id):
    stock = Stock.objects.get(id=stock_id)
    return render(request, 'stock_forms/stock_detail.html', {'stock': stock})

@login_required
def get_stocks(request):
    stocks = Stock.objects.filter(user=request.user)
    return render(request, 'stock_forms/stock_list.html', {'stocks': stocks})

def new_stock(request):
    if request.method == "POST":
        form = StockForm(request.POST)
        if form.is_valid():
            stock = form.save(commit=False)
            stock.user = request.user
            stock.save()
            return get_stocks(request)
    else:
        form = StockForm()
    return render(request, 'stock_forms/stock_form.html', {'form': form, 'type_of_request': 'New'})

def edit_stock(request, stock_id):
    stock = get_stock(stock_id)
    if request.method == "POST":
        form = StockForm(request.POST, instance=stock)
        if form.is_valid():
            stock = form.save(commit=False)
            stock.user = request.user
            stock.save()
            return get_stocks(request)
    else:
        form = StockForm(instance=stock)
    return render(request, 'stock_forms/stock_form.html', {'form': form, 'type_of_request': 'Edit'})

def delete_stock(request, stock_id):
    if request.method == "POST":
        stock = get_stock(stock_id)
        stock.delete()
    return get_stocks(request)

def stock_search_generator(symbol):
    return f"https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol={symbol}&apikey={stock_api_key}"

def stock_quote(request, stock_id):
    stock = get_stock(stock_id)
    stock_for_quote = stock_search_generator(stock.symbol)
    r = requests.get(stock_for_quote)
    response = r.json()
    content = {
        'opening_price': response['Global Quote']['02. open'],
        'high_price': response['Global Quote']['03. high'],
        'low_price': response['Global Quote']['04. low'],
        'current_price': response['Global Quote']['05. price'],
        'previous_close_price': response['Global Quote']['08. previous close'],
        'price_change': response['Global Quote']['09. change'],
        'price_change_percent': response['Global Quote']['10. change percent'],
        'my_total_stock_price': float(response['Global Quote']['05. price']) * stock.shares,
        'stock': stock
    }
    return render(request, 'stock_forms/stock_quote.html', content)


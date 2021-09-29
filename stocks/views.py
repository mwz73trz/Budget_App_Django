from django.shortcuts import render
import requests
from .models import Stock
from .forms import StockForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

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


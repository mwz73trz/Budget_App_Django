from django.shortcuts import render
import requests
from .models import Debt, Credit
from .forms import DebtForm, CreditForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

def get_debt(debt_id):
    return Debt.objects.get(id=debt_id)

def get_credit(credit_id):
    return Credit.objects.get(id=credit_id)

@login_required
def get_debt_credit_list(request):
    debits = Debt.objects.filter(user=request.user)
    credits = Credit.objects.filter(user=request.user)
    return render(request, 'budget.html', {'debits': debits, 'credits': credits})


def new_debt(request):
    if request.method == "POST":
        form = DebtForm(request.POST)
        if form.is_valid():
            debt = form.save(commit=False)
            debt.user = request.user
            debt.save()
            return (get_debt_credit_list(request))
    else:
        form = DebtForm()
    return render(request, 'debt_form.html', {'form': form, 'type_of_request': 'New'})

def edit_debt(request, debt_id):
    debt = get_debt(debt_id)
    if request.method == "POST":
        form = DebtForm(request.POST, instance=debt)
        if form.is_valid():
            debt = form.save(commit=False)
            debt.user = request.user
            debt.save()
            return get_debt_credit_list(request)
    else:
        form = DebtForm(instance=debt)
    return render(request, 'debt_form.html', {'form': form, 'type_of_request': 'Edit'})

def delete_debt(request, debt_id):
    if request.method == "POST":
        debt = get_debt(debt_id)
        debt.delete()
    return get_debt_credit_list(request)

def new_credit(request):
    if request.method == "POST":
        form = CreditForm(request.POST)
        if form.is_valid():
            credit = form.save(commit=False)
            credit.user = request.user
            credit.save()
            return (get_debt_credit_list(request))
    else:
        form = CreditForm()
    return render(request, 'credit_form.html', {'form': form, 'type_of_request': 'New'})

def edit_credit(request, credit_id):
    credit = get_credit(credit_id)
    if request.method == "POST":
        form = CreditForm(request.POST, instance=credit)
        if form.is_valid():
            credit = form.save(commit=False)
            credit.user = request.user
            credit.save()
            return get_debt_credit_list(request)
    else:
        form = CreditForm(instance=credit)
    return render(request, 'credit_form.html', {'form': form, 'type_of_request': 'Edit'})

def delete_credit(request, credit_id):
    if request.method == "POST":
        credit = get_credit(credit_id)
        credit.delete()
    return get_debt_credit_list(request)

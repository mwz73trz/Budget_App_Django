from django import forms
from .models import Debt, Credit

class DebtForm(forms.ModelForm):
    class Meta:
        model = Debt
        fields = ('name', 'amount')

class CreditForm(forms.ModelForm):
    class Meta:
        model = Credit
        fields = ('name', 'amount')
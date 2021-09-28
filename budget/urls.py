from django.urls import path
from . import views

app_name = 'budget'

urlpatterns = [
    path('', views.get_debt_credit_list, name='debt_credit_list'),
    path('new_debt', views.new_debt, name='new_debt'),
    path('<int:debt_id>/edit', views.edit_debt, name='edit_debt'),
    path('<int:debt_id>/delete', views.delete_debt, name='delete_debt'),
    path('new_credit', views.new_credit, name='new_credit'),
    path('new_credit/<int:credit_id>/edit', views.edit_credit, name='edit_credit'),
    path('delete_credit/<int:credit_id>/delete', views.delete_credit, name='delete_credit'),
    path('annual_totals', views.get_annual_totals, name='annual_totals'),
]

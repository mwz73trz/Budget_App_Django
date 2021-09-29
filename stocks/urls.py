from django.urls import path
from . import views

app_name = 'stocks'

urlpatterns = [
    path('stocks/', views.get_stocks, name='get_stocks'),
    path('stocks/new_stock', views.new_stock, name='new_stock'),
    path('stocks/<int:stock_id>', views.get_stock_detail, name='get_stock_detail'),
    path('stocks/<int:stock_id>/edit', views.edit_stock, name='edit_stock'),
    path('stocks/<int:stock_id>/delete', views.delete_stock, name='delete_stock'),
]
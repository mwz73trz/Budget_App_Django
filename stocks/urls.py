from django.urls import path
from . import views

app_name = 'stocks'

urlpatterns = [
    path('', views.get_stocks, name='get_stocks'),
    path('stocks/new_stock', views.new_stock, name='new_stock'),
    path('stocks/<int:stock_id>', views.get_stock_detail, name='get_stock_detail'),
    path('stocks/<int:stock_id>/edit', views.edit_stock, name='edit_stock'),
    path('stocks/<int:stock_id>/delete', views.delete_stock, name='delete_stock'),
    path('stocks/stock_quote/<int:stock_id>', views.stock_quote, name='stock_quote'),
    path('stock_overview', views.stock_overview, name='stock_overview'),
]
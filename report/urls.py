from django.urls import path
from . import views

urlpatterns = [
    path('stock_report/', views.stock_report, name='stock_report'),
    path('sales_report/', views.sales_report, name='sales_report'),
    
   
]
from django.urls import path
from . import views


urlpatterns = [
    path('',views.index,name='index'),
    path('stock/', views.stockdetails, name='stockdetails.html'),


]
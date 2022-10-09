from django import urls
from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from .import views

#app_name for food's urls.py
app_name= 'food'
urlpatterns = [
    path('', views.index, name='index'),
    path('index/', views.index, name='index'),
    path('item/', views.item, name='item'),

    #/food/1   dispay single item
    path('<int:itemId>/', views.detail, name='detail'),
    #add item to the list 
    path('addItem/', views.addItem, name='addItem'), 
    #edit item
    path('update/<int:itemId>/',views.updateItem, name='updateItem'),
    #delete item
    path('delete/<int:itemId>/', views.deleteItem, name='deleteItem'),


]

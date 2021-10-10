from django.contrib import admin
from django.urls import path

from .views import ShopListView


app_name = 'shop_list'
urlpatterns = [
    path('', ShopListView.as_view(), name='shop-list'),
]

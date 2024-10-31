from django.contrib import admin
from django.urls import path
from .views import ProductListView

app_name = 'store'

urlpatterns = [
    path('category/<slug:slug>/', ProductListView.as_view(), name='category')
]


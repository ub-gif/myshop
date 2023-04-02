from django.urls import path
from shop import views

urlpatterns = [
    path('items/', views.item_list, name='item-list'),
    path('', views.home, name='home'),
]
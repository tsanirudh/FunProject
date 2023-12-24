from django.urls import path
from .views import item_list

urlpatterns = [
    path('api/items/', item_list, name='item-list'),
]

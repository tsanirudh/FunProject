from django.urls import path
from .views import item_list
from .views import connect_to_macbook


urlpatterns = [
    path('api/items/', item_list, name='item-list'),
    path('api/connect-to-macbook/', connect_to_macbook, name='connect-to-macbook'),
]

from django.urls import path
from .views import ItemList, item_list, welcome

urlpatterns = [
    path('api/items/', item_list, name='item-list'),
    path('welcome/', welcome, name='welcome'),
    path('api/items/', ItemList.as_view(), name='item-list'),
     
]

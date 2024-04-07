from django.urls import path
from .views import ItemList, item_list, welcome, connect_to_macbook, send_command, store_location, start_ollama

urlpatterns = [
    path('api/items/', item_list, name='item-list'),
    path('welcome/', welcome, name='welcome'),
    path('api/items/', ItemList.as_view(), name='item-list'),
    path('api/connect-to-macbook/', connect_to_macbook, name='connect-to-macbook'),
    path('api/store-location/', store_location, name='store-location'),
    path('api/start-ollama/', start_ollama, name='start-ollama'),
    path('api/send-command/', send_command, name='send-command'),
    
     
]

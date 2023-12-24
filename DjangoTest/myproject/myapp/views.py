import json
from django.shortcuts import render
from django.http import JsonResponse
from .models import Item
from rest_framework import generics
from .serializers import ItemSerializer
from django.middleware import csrf

items = []

#  prevent csrf check for this view only 
class ItemList(generics.ListCreateAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

def item_list(request):
    items = Item.objects.all()
    
    # Example print statement
    if request.method == 'POST': 
        payload = json.loads(request.body)
        print("Debug --->>>>>>>>: Items in item_list view:", payload)
        item = Item.objects.create(name=payload['foo'])
        item.save()
        return JsonResponse({"message": "Item added successfully!"})
    else:
        print("Debug --->>>>>>>>: :", items)
        data = {
            'data': list(items.values('id', 'name')),
            "credentials": {
                "username": "test",
                "password": "test",
                "csrf": csrf.get_token(request)
            },
        }
        # also pass in data and csrf token
        return JsonResponse(data)



def addItem(request):    
    item = Item.objects.create(name="Item 1", description="Item 1 description")
    item.save()
    
    # Example print statement
    print("Debug: Item added in addItem view:", item)

    return JsonResponse({"message": "Item added successfully!"})

def welcome(request):
    return render(request, 'welcome.html')

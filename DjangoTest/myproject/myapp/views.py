import json
import sys
import paramiko
from django.shortcuts import render
from django.http import JsonResponse
from .models import Item
from rest_framework import generics
from .serializers import ItemSerializer
from django.middleware import csrf
from django.http import JsonResponse
import paramiko
print("Python version", sys.path)


items = []

ssh_client = paramiko.SSHClient()
askOllama = ""
ipAddress = ""
port = ""
# Function to establish an SSH connection to your MacBook
def connect_to_macbook():
    # Update the following variables with your MacBook's SSH details
    hostname = 'Anirudhs-MBP.home'
    port = 22
    username = 'anirudhsomadas'
    password = 'Iamani1234$'

    # Create an SSH client
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    try:
        # Connect to the MacBook
        ssh_client.connect(hostname, port, username, password)
        print("Connected to MacBook via SSH")

        ipAddress = ssh_client.get_transport().sock.getpeername()[0]
        print("IP Address:", ipAddress)

        # Run a command on the server
        command = "ls -l"
        stdin, stdout, stderr = ssh_client.exec_command(command)

        # Get the command output
        output = stdout.read().decode('utf-8')
        print("Command output:", output)
    

        # now start ollama ssh server
        command = "ollama serve --port 5000"
        desiredPort = 5000
        # run ollama in the desired port
        stdin, stdout, stderr = ssh_client.exec_command(command)

        # Get the command output
        output = stdout.read().decode('utf-8')
        print("Command output:", output)

        return JsonResponse({"message": "Connected to MacBook via SSH", "output": output})
    
    
    except Exception as e:
        print(f"Error connecting to MacBook: {str(e)}")
        return JsonResponse({"message": f"Error connecting to MacBook: {str(e)}"})
        # Close the SSH client
        

#  prevent CSRF check for this view only

def send_command(request):
    # Function to send a command to your MacBook
    ip = "192.168.1.155"
    port = 11434
    # //send a command to the ollama server
    # //get the output
    # //return the output

    print("ip address is", ip)

    # Update the following variables with your MacBook's SSH details
    

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
                "csrf": csrf.get_token(request),
            },
        }

        # Establish SSH connection to MacBook
        connect_to_macbook()

        # Also pass in data and CSRF token
        return JsonResponse(data)

def connectToMacbook(request):
    # Function to connect to MacBook
    connect_to_macbook()

    # Additional logic for your connectToMacbook view
    # ...

def addItem(request):
    item = Item.objects.create(name="Item 1", description="Item 1 description")
    item.save()

    # Example print statement
    print("Debug: Item added in addItem view:", item)

    return JsonResponse({"message": "Item added successfully!"})

def welcome(request):
    return render(request, 'welcome.html')

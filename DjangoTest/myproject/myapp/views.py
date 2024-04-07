import json
import sys
import paramiko
import subprocess
from django.shortcuts import render
from django.http import JsonResponse
from .models import Item
from rest_framework import generics
from .serializers import ItemSerializer
from django.middleware import csrf
from django.http import JsonResponse
import paramiko
import socket
from langchain.llms import Ollama

ollama = Ollama(base_url='http://localhost:11434', model="gemma")
items = []

ssh_client = paramiko.SSHClient()
askOllama = ""
ipAddress = ""
port = ""
storedLocations = []
# Function to establish an SSH connection to your MacBook



def store_location(request):
    if request.method == 'POST':
        payload = json.loads(request.body)
        # if the payload has an item named data
        if 'data' in payload:
            data = json.loads(payload['data'])  # Convert data to a dictionary
            print("This is from data", data)
            print(data['location'])
            location = data['location']
            markDescription = data['markDescription']
            markers = data['markers']
            # Store the location in the storedLocations array
            storedLocations.append({
                'location': location,
                'markDescription': markDescription,
                'markers': markers
            })
        return JsonResponse({"message": "Location stored successfully!"})
    else:
        return JsonResponse({"storedLocations": storedLocations})

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

        ipAddress = ssh_client.get_transport().sock.getpeername()[0]

        # Run a command on the server
        command = "ls -l"
        stdin, stdout, stderr = ssh_client.exec_command(command)

        # Get the command output
        output = stdout.read().decode('utf-8')
    

        # now start ollama ssh server
        command = "ollama serve --port 5000"
        desiredPort = 5000
        # run ollama in the desired port
        stdin, stdout, stderr = ssh_client.exec_command(command)

        # Get the command output
        output = stdout.read().decode('utf-8')

        return JsonResponse({"message": "Connected to MacBook via SSH", "output": output})
    
    
    except Exception as e:
        return JsonResponse({"message": f"Error connecting to MacBook: {str(e)}"})
        # Close the SSH client
        

#  prevent CSRF check for this view only
    

def start_ollama(request):
    # Check if ollama server is already running on port 11434
    ip = "127.0.0.1"
    port = 11434
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    result = sock.connect_ex((ip, port))
    if result == 0:
        return JsonResponse({"message": "Ollama server is already running on port 11434"})
    
    # Run the command to start ollama server with gemma model
    print("Starting Ollama server")
    command = 'ollama serve gemma:2b'
    subprocess.run(command, shell=True)
    return JsonResponse({"message": "Ollama server started successfully!"})

    # run the command in this windows laptop 

def send_command(request):

    payload = json.loads(request.body)
    print(" --->>>>>>>Sending command to Ollama server", payload)
    input = payload['input']
    response = ollama(input)
    return JsonResponse({"response": response})

    # Update the following variables with your MacBook's SSH details
    

class ItemList(generics.ListCreateAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

def item_list(request):
    items = Item.objects.all()

    # Example print statement
    if request.method == 'POST':
        payload = json.loads(request.body)
        item = Item.objects.create(name=payload['foo'])
        item.save()
        return JsonResponse({"message": "Item added successfully!"})
    else:
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

    return JsonResponse({"message": "Item added successfully!"})

def welcome(request):
    return render(request, 'welcome.html')

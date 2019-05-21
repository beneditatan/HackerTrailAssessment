from rest_framework import status
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .serializers import ClientSerializer, FeatureSerializer
from .models import Client, Feature

import json

# Create your views here.
def get_clients(request):
    if request.method == "GET":
        clients = Client.objects.all()
        serializer = ClientSerializer(clients, many=True)
        msg = {"data": serializer.data}
        return HttpResponse(json.dumps(msg), status=200)
    else:
        msg = {"message": "Method Not Allowed"}
        return HttpResponse(json.dumps(msg), status=405)

@csrf_exempt
def create_feature(request):
    if request.method == "POST":
        serializer = FeatureSerializer(data=request.POST)
        if serializer.is_valid():
            serializer.save()
            return HttpResponse(json.dumps(serializer.data), status=201)
        return HttpResponse(json.dumps(serializer.errors), status=400)
    else:
        msg = {"message": "Method Not Allowed"}
        return HttpResponse(json.dumps(msg), status=405)

def get_client_priorities(request):
    if request.method == "GET":
        client_id = request.GET['client']
        client = Client.objects.get(id=client_id)
        features = Feature.objects.filter(client=client)
        prio = [i for i in range(1, len(features)+2)]
        json_data = {"data": prio}
        return HttpResponse(json.dumps(json_data), status=200)
    else:
        msg = {"message": "Method Not Allowed"}
        return HttpResponse(json.dumps(msg), status=405)

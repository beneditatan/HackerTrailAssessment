from rest_framework import status
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .serializers import ClientSerializer, FeatureSerializer
from .models import Client

import json

# Create your views here.
def get_clients(request):
    if request.method == "GET":
        clients = Client.objects.all()
        serializer = ClientSerializer(clients, many=True)
        msg = {"data": serializer.data}
        return HttpResponse(json.dumps(msg), status=200)
    else:
        msg = {"message": "Bad request"}
        return HttpResponse(json.dumps(msg), status=400)

@csrf_exempt
def create_feature(request):
    if request.method == "POST":
        serializer = FeatureSerializer(data=request.POST)
        if serializer.is_valid():
            serializer.save()
            return HttpResponse(json.dumps(serializer.data), status=201)
        return HttpResponse(json.dumps(serializer.errors), status=400)
    else:
        msg = {"message": "Bad request"}
        return HttpResponse(json.dumps(msg), status=400)

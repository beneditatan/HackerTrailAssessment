from rest_framework import serializers
from .models import Client, Feature

class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ('id', 'name')


class FeatureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feature
        fields = "__all__"

    def create(self, data):
        return Feature.objects.create(**data)
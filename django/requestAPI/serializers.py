from django.db.models import Q, F
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
        print(data)
        client_priority = data['client_priority']
        # get all the features requested by the client
        features_client = Feature.objects.filter(client=data['client'])
        num_of_features = len(features_client)

        # reorder feature based on its priority
        if client_priority < num_of_features:
            to_sort = [f for f in features_client if f.client_priority >= client_priority]
            for feature in to_sort:
                feature.client_priority = F('client_priority') + 1
                feature.save()

        return Feature.objects.create(**data)
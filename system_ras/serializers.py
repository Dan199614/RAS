from rest_framework import serializers
from .models import *


class L110KvaB1Serializer(serializers.ModelSerializer):
    class Meta:
        model = L110KvaB1
        fields = '__all__'

        def get_status(self, obj: L110KvaB1):
            return obj.get_status_display()


class L110KvaB2Serializer(serializers.ModelSerializer):
    class Meta:
        model = L110KvaB2
        fields = '__all__'

        def get_status(self, obj: L110KvaB2):
            return obj.get_status_display()


class L110KvaB3Serializer(serializers.ModelSerializer):
    class Meta:
        model = L110KvaB3
        fields = '__all__'

        def get_status(self, obj: L110KvaB3):
            return obj.get_status_display()


class L110KvdB1Serializer(serializers.ModelSerializer):
    class Meta:
        model = L110KvdB1
        fields = '__all__'

        def get_status(self, obj: L110KvdB1):
            return obj.get_status_display()


class L110KvdB2Serializer(serializers.ModelSerializer):
    class Meta:
        model = L110KvdB2
        fields = '__all__'

        def get_status(self, obj: L110KvdB2):
            return obj.get_status_display()


class L110KvdB3Serializer(serializers.ModelSerializer):
    class Meta:
        model = L110KvdB3
        fields = '__all__'

        def get_status(self, obj: L110KvdB3):
            return obj.get_status_display()


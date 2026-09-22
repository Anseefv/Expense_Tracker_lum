from rest_framework import serializers
from .models import*
from django.contrib.auth.models import User


class RegisterSerializer(serializers.Serializer):
    username=serializers.CharField()
    email=serializers.EmailField()
    password=serializers.CharField()




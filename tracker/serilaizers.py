from rest_framework import serializers
from .models import*
from django.contrib.auth.models import User


class RegisterSerializer(serializers.Serializer):
    username=serializers.CharField()
    email=serializers.EmailField()
    password=serializers.CharField()


class ExpensesSerializer(serializers.ModelSerializer):
    class Meta:
        model=Expenses
        fields='__all__'
        read_only_fields=['owner']


class SummerySerializer(serializers.Serializer):
    category=serializers.CharField()
    amount_sum=serializers.IntegerField()





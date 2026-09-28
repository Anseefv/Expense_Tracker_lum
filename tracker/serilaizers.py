from rest_framework import serializers
from .models import*
from django.contrib.auth.models import User


class RegisterSerializer(serializers.Serializer):
    username=serializers.CharField()
    email=serializers.EmailField()
    password=serializers.CharField()


class ExpensesSerializer(serializers.ModelSerializer):
    # owner=serializers.StringRelatedField(read_only=True)
    owner=serializers.SerializerMethodField()
    class Meta:
        model=Expenses
        fields='__all__'
        read_only_fields=['owner']
    def get_owner(self,obj):
        return obj.owner.username


class SummerySerializer(serializers.Serializer):
    category=serializers.CharField()
    amount_sum=serializers.IntegerField()





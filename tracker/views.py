from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from rest_framework import status



from django.contrib.auth.models import User
from .models import*
from .serilaizers import*



class RegisterViewSet(ViewSet):
    def create(self,request):
        ser=RegisterSerializer(data=request.data)
        if ser.is_valid():
            User.objects.create_user(**ser.validated_data)
            return Response(ser.data,status=status.HTTP_201_CREATED)
        return Response(ser.errors,status=status.HTTP_400_BAD_REQUEST)







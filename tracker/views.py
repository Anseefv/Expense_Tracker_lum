from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import BasicAuthentication,TokenAuthentication
from rest_framework.views import APIView
from django.db.models import Sum




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


class ExpenseViewset(ViewSet):

    authentication_classes=[TokenAuthentication]
    permission_classes=[IsAuthenticated]

    def create(self,request):
        ser=ExpensesSerializer(data=request.data)
        if ser.is_valid():
            ser.save(owner=request.user)
            return Response(ser.data,status=status.HTTP_201_CREATED)
        return Response(ser.errors,status=status.HTTP_400_BAD_REQUEST)

    def list(self,request):
        obj=Expenses.objects.filter(owner=request.user)
        ser=ExpensesSerializer(obj,many=True)
        return Response(ser.data)

    def destroy(self,request,pk):
        data=Expenses.objects.get(pk=pk,owner=request.user).delete()
        return Response({"msg":"deleted"},status=status.HTTP_204_NO_CONTENT)

    def update(self,request,pk):
        data=Expenses.objects.get(pk=pk,owner=request.user)
        ser=ExpensesSerializer(data,data=request.data)
        if ser.is_valid():
            ser.save()
            return Response(ser.data)
        return Response(ser.errors,status=status.HTTP_400_BAD_REQUEST)

    def partial_update(self,request,pk):
        data=Expenses.objects.get(pk=pk,owner=request.user)
        ser=ExpensesSerializer(data,data=request.data,partial=True)
        if ser.is_valid():
            ser.save()
            return Response(ser.data)
        return Response(ser.errors,status=status.HTTP_400_BAD_REQUEST)


    def retrieve(self, request, pk):
        try:
            data=Expenses.objects.get(pk=pk,owner=request.user)
        except Exception :
            return Response({"error":"not found"},status=status.HTTP_404_NOT_FOUND)
        ser=ExpensesSerializer(data)
        return Response(ser.data)

from django.db.models import Sum

class SummeryApiView(APIView):

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):

        data = Expenses.objects.filter(
            owner=request.user
        ).values('category').annotate(
            amount_sum=Sum('amount')
        )

        ser = SummerySerializer(data, many=True)

        return Response(ser.data)



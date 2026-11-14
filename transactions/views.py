from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework import authentication,permissions
from transactions.models import Expense
from transactions.serializers import ExpenseSerializer
from rest_framework.response import Response


class ExpenseListCreateView(APIView):

    authentication_classes=[authentication.BasicAuthentication]

    permission_classes=[permissions.IsAuthenticated]


    def get(self,request):

# we take the user which gives the username and password to get the list of expenses so that only his expenses are listed
        auth_user = request.user

        qs = Expense.objects.filter(owner=auth_user)

        serializer_instance = ExpenseSerializer(qs,many=True)

        return Response(serializer_instance.data)

    def post(self,request):

        form_data = request.data

        auth_user = request.user

        serializer_instance = ExpenseSerializer(data=form_data)

        if serializer_instance.is_valid():

# owner wont be saved in form data because wo dont give owner so we need to give it in save because it is required to get and create expense
            serializer_instance.save(owner=auth_user)

            return Response(serializer_instance.data)

        else:

            return Response(serializer_instance.errors)
        
    
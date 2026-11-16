from django.shortcuts import render,get_object_or_404

# Create your views here.
from rest_framework.views import APIView
from rest_framework import authentication,permissions
from transactions.models import Expense
from transactions.serializers import ExpenseSerializer
from rest_framework.response import Response
from transactions.permissions import IsOwner


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
        

class ExpenseRetrieveUpdateDeleteView(APIView):

    authentication_classes = [authentication.BasicAuthentication]

    # permission_classes = [permissions.IsAuthenticated]

# custom permisssion for only owner to take only his detail and others
    permission_classes = [IsOwner]


    def get(self,request,pk=None):

        qs = get_object_or_404(Expense,id=pk)

# after taking object we should chk if request was send by its owner or other,if other reject
        self.check_object_permissions(request,qs)

        serializer_instance = ExpenseSerializer(qs)

        return Response(serializer_instance.data)

    def put(self,request,pk=None):

        instance = get_object_or_404(Expense,id=pk)

        self.check_object_permissions(request,instance)

        form_data = request.data

        serializer_instance = ExpenseSerializer(data=form_data,instance=instance)

        if serializer_instance.is_valid():

            serializer_instance.save()

            return Response(serializer_instance.data)

        else:

            return Response(serializer_instance.errors)

    def delete(self,request,pk=None):

        qs = get_object_or_404(Expense,id=pk)

        self.check_object_permissions(request,qs)

        qs.delete()

        return Response({"message":"deleted..."})

    
from datetime import datetime
from django.db.models import Sum

class ExpenseSummaryView(APIView):


    authentication_classes =[authentication.BasicAuthentication]

    permission_classes=[permissions.IsAuthenticated]

    def get(self,request):

        auth_user_expenses = Expense.objects.filter(owner=request.user)

        response_data={
            "todays_total":0,
            "monthly_total":0
        }

        cur_date = datetime.today().date()

        todays_total=auth_user_expenses.filter(
                                                created_at__date = cur_date
                                                ).values("amount").aggregate(total=Sum("amount")).get("total")

        #todays_total=3200

        response_data["todays_total"]= todays_total

        return Response(response_data)
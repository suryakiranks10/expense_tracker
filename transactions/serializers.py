from rest_framework import serializers
from transactions.models import Expense

class ExpenseSerializer(serializers.ModelSerializer):

    class Meta:

        model = Expense

# to take all fields from expense model 
        fields = "__all__"

# to exclude the read only fields from expense they arent added in form data which we give in apidoc post but we need to save them
        read_only_fields = ["id","owner","created_at"]
from django.db import models

# Create your models here.
from accounts.models import User

#Expense [title,category,amount,description,owner[FK(User)],created_at,bill_image]

class Expense(models.Model):

    title = models.CharField(max_length=200,null=True)

    CATEGORY_CHOICES = [
        ("food", "Food"),
        ("fuel", "Fuel"),
        ("health", "Health"),
        ("shopping", "Shopping"),
        ("travel", "Travel"),
        ("education", "Education"),
        ("rent", "Rent"),
        ("bills", "Bills & Utilities"),
        ("entertainment", "Entertainment"),
        ("groceries", "Groceries"),
        ("personal", "Personal Care"),
        ("other", "Other"),
    ]

    category = models.CharField(max_length=20,choices=CATEGORY_CHOICES,default="food")

    amount = models.DecimalField(max_digits=10,decimal_places=2)

    description = models.TextField(null=True)

    PAYMENT_CHOICES=(
        ("upi","upi"),
        ("cash","cash")
    )

    owner = models.ForeignKey(User,on_delete=models.CASCADE)

    payment_method = models.CharField(choices=PAYMENT_CHOICES,default="upi",max_length=200)

    created_at = models.DateTimeField(auto_now_add=True)

    bill_image = models.ImageField(upload_to="bills",null=True)



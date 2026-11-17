"""
URL configuration for expense_tracker project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from accounts.views import SignUpView

from transactions.views import ExpenseListCreateView
from transactions.views import ExpenseRetrieveUpdateDeleteView
from transactions.views import ExpenseSummaryView

from rest_framework.authtoken.views import ObtainAuthToken

urlpatterns = [
    path('admin/', admin.site.urls),


#Accounts
    path("accounts/register/",SignUpView.as_view()),


#Expenses
    path("expenses/",ExpenseListCreateView.as_view()),
    path("expenses/<int:pk>/",ExpenseRetrieveUpdateDeleteView.as_view()),
    path("expenses/summary/",ExpenseSummaryView.as_view()),

#auth token
path("token/",ObtainAuthToken.as_view()),

]

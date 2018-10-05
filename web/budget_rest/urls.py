"""budget_rest URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from .views import (
        RegisterApiView,
        UserApiView,
        BudgetListApiView,
        TransactionListApiView,
        TransactionDetailApiView,
        BudgetDetailApiView
    )
from django.urls import path
from rest_framework.authtoken import views

urlpatterns = [
    path('user/<int:pk>', UserApiView.as_view(), name='user-detail'),
    path('register', RegisterApiView.as_view(), name='register'),
    path('login', views.obtain_auth_token, name='login'),
    path('budget/', BudgetListApiView.as_view(), name='budget'),
    path('budget/<int:pk>', BudgetDetailApiView.as_view(), name='budget_detail'),
    path('transaction/', TransactionListApiView.as_view(), name='transaction'),
    path('transaction/<int:pk>', TransactionDetailApiView.as_view(), name='transaction_detail'),
    ]


# urlpatterns = [
#     path('user/<int:pk>', UserApiView.as_view(), name='user-detail'),
#     path('register', RegisterApiView.as_view(), name='register'),
#     path('login', views.obtain_auth_token),
#     path('category/', CategoryListApiView.as_view(), name='category-list-api'),
#     path('category/<int:pk>', CategoryDetailApiView.as_view(), name='category-detail-api'),
#     path('card/', CardListApiView.as_view(), name='card-list-api'),
#     path('card/<int:pk>', CardDetailApiView.as_view(), name='card-detail-api'),
# ]

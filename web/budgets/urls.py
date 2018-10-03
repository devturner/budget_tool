from django.contrib import admin
from django.urls import path
from .views import home_view, BudgetListView, TransactionDetailView
from django.conf.urls import include

urlpatterns = [
	path('admin/', admin.site.urls),
    path('', home_view, name='home'),
    path('accounts/', include('django_registration.backends.activation.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('budget', BudgetListView.as_view(), name='budget_view'),
    path('budget/<int:id>', TransactionDetailView.as_view(), name='transaction_detail'),
]

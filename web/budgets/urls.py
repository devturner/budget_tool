from django.contrib import admin
from django.urls import path
from .views import home_view, BudgetListView, TransactionDetailView, BudgetCreateView, TransactionCreateView
from django.conf.urls import include


urlpatterns = [
	path('admin/', admin.site.urls),
    path('', home_view, name='home'),
    path('accounts/', include('django_registration.backends.activation.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('budget', BudgetListView.as_view(), name='budget_view'),
    path('budget/new', BudgetCreateView.as_view(), name='create_budget'),
    path('budget/<int:id>', TransactionDetailView.as_view(), name='transaction_detail'),
    path( 'transaction/new', TransactionCreateView.as_view(), name="create_transaction"),
    path('api/v1/', include('budget_rest.urls')),
]

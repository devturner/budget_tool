from django.contrib.auth.models import User
from rest_framework import serializers
from budgets.models import Budget, Transaction

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password', 'first_name', 'last_name')

    def create(self, validated_data):
        user = super().create({
            'username': validated_data['username'],
            'email': validated_data['email'],
        })

        user.set_password(validated_data['password'])
        user.save()
        return user


class TransactionsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Transaction
        fields = ('description', 'amount')


class BudgetSerializer(serializers.HyperlinkedModelSerializer):
    transactions = TransactionsSerializer(many=True, read_only=True)

    class Meta:
        model = Budget
        fields = ('name', 'total_budget', 'remaining_budget', 'transactions')

from django.contrib.auth.models import User
from django.dispatch import receiver
from django.utils import timezone
from django.db import models


class Budget(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='budget')
    name = models.CharField(max_length=180, default='Untitled')
    total_budget = models.FloatField()
    remaining_budget = models.FloatField(blank=True, null=True)
    date_created = models.DateField(auto_now_add=True)
    date_modified = models.DateField(auto_now=True)

    # @property
    # def remaining_budget(self):
    #     return self.total_budget - Transaction.object.filter(amount = amount)

    def __repr__(self):
        return '<Budget: {}>'.format(self.name)

    def __str__(self):
        return '{}'.format(self.name)


class Transaction(models.Model):
    budget = models.ForeignKey(Budget, on_delete=models.CASCADE, related_name='transaction')
    amount = models.FloatField()
    description = models.TextField(blank=True, null=True)

    TRANSACTION_TYPE = (
        ('WITHDRAWAL', 'withdrawal'),
        ('DEPOSIT', 'deposit'),
    )
    type = models.CharField(
        max_length=10,
        choices=TRANSACTION_TYPE,
    )

    def __repr__(self):
        return '<Transaction: {} | {}>'.format(self.amount, self.description)

    def __str__(self):
        return '{} | {}'.format(self.amount, self.description)

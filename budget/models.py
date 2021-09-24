from django.db import models
from django.contrib.auth.models import User

class Debt(models.Model):
    name = models.CharField(max_length=150)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='debits')

    def __str__(self):
        return f"{self.name} totals ${self.amount}"

    @property
    def total_debt(self):
        return sum(self.amount)

class Credit(models.Model):
    name = models.CharField(max_length=150)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='credits')

    def __str__(self):
        return f"{self.name} totals ${self.amount}"

    @property
    def total_credit(self):
        return sum(self.amount)


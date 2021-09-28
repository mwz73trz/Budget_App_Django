from django.db import models
from django.contrib.auth.models import User

class Debt(models.Model):
    name = models.CharField(max_length=150)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='debits')

    def __str__(self):
        return f"{self.name} totals ${self.amount}"

    @property
    def year_total(self):
        annual_amount = self.amount * 12
        return annual_amount

class Credit(models.Model):
    name = models.CharField(max_length=150)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='credits')

    def __str__(self):
        return f"{self.name} totals ${self.amount}"

    @property
    def year_total(self):
        annual_amount = self.amount * 12
        return annual_amount


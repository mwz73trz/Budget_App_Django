from django.db import models
from django.contrib.auth.models import User

class Stock(models.Model):
    name = models.CharField(max_length=150)
    symbol = models.CharField(max_length=4)
    shares = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='stocks')

    def __str__(self):
        return f"{self.name}"


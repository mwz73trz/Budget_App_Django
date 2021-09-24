from django.contrib import admin
from .models import Debt, Credit

admin.site.register([Debt, Credit])


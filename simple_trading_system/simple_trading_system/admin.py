from django.contrib import admin
from .models import Stock, Trader,Transaction

admin.site.register(Stock)
admin.site.register(Trader)
admin.site.register(Transaction)
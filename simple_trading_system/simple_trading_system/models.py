from django.db import models

class Stock(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()

    def __str__(self):
        return self.name

class Trader(models.Model):
    firstName = models.CharField(max_length=150)
    lastName = models.CharField(max_length=150)
    def __str__(self):
        return self.firstName + " "  + self.lastName

class Transaction(models.Model):
    userId = models.ForeignKey(Trader, on_delete=models.CASCADE)
    stockId = models.ManyToManyField(Stock)
    quantity = models.IntegerField()
    
    def __str__(self):
        return self.name

    
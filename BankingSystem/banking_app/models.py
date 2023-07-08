from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(primary_key=True,max_length=100)
    password = models.CharField(max_length=100)
    email = models.EmailField()
    balance = models.DecimalField(max_digits=10,decimal_places=2)

class Transaction(models.Model):
    from_username = models.CharField(max_length=100)
    to_username = models.CharField(max_length=100)
    transaction_id = models.CharField(primary_key=True,max_length=100)
    amount = models.DecimalField(max_digits=10,decimal_places=2)

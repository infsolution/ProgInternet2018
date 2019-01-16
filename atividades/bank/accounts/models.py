from django.db import models

class Account(models.Model):
	owner = models.CharField(max_length=200)
	balance = models.DecimalField(max_digits=5, decimal_places=2)
	creation_date = models.DateTimeField()

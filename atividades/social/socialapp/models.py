from django.db import models

class Address(models.Model):
	street = models.CharField(max_length=200)
	suite = models.CharField(max_length=200)
	city = models.CharField(max_length=200)
	zipcode = models.CharField(max_length=12)

class Profile(models.Model):
	address = models.ForeignKey(Address,related_name='address',on_delete=models.CASCADE)
	name = models.CharField(max_length=200)
	email = models.CharField(max_length=200) 
	def __str__(self):
		return self.name

class Comment(models.Model):
	



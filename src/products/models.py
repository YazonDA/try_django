from django.db import models
from django.urls import reverse


class Product(models.Model):
	name = models.CharField(max_length=32)
	status = models.IntegerField() #max_digits=1, decimal_places=None
	# DANGER		= 0
	# IMPORTANT	= 1
	# ATTENTION	= 2
	# MAYBE		= 3
	group = models.CharField(max_length=16)
	price = models.DecimalField(max_digits=6, decimal_places=2)

	def get_absolute_url(self):
		return reverse('products:product-list')
		# return reverse('products:product-list', kwargs={'id': self.id})

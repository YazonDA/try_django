from django.db import models


class ShopList(models.Model):
	name = models.CharField(max_length=32)
	status = models.IntegerField() #max_digits=1, decimal_places=None
	# DANGER		= 0
	# IMPORTANT	= 1
	# ATTENTION	= 2
	# MAYBE		= 3

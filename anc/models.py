from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class UserProfile(models.Model):
	user = models.OneToOneField(User, null = True)
	phone = models.BigIntegerField(blank = True, null = True)
	secret_pin = models.IntegerField(blank = True, null = True)
	login = models.IntegerField(default = 0)
	key = models.IntegerField(default = 1)

	def __str__(self) :
		return str(self.user)

class Item(models.Model):
	name = models.CharField(max_length = 20, blank = True, default ='')
	price = models.IntegerField(default=0)

	def __str__(self):
		return self.name

class Order(models.Model):
	user = models.ForeignKey(User, on_delete = models.CASCADE, null = True)
	key = models.IntegerField(default = 1)
	item1 = models.ForeignKey(Item, on_delete = models.CASCADE, related_name = 'item1', null = True, default = '')
	quantity1 = models.IntegerField(default = 0)
	item2 = models.ForeignKey(Item, on_delete = models.CASCADE, related_name = 'item2', null = True, default = '')
	quantity2 = models.IntegerField(default = 0, null = True)
	item3 = models.ForeignKey(Item, on_delete = models.CASCADE, related_name = 'item3', null = True, default = '')
	quantity3 = models.IntegerField(default = 0, null = True)
	item4 = models.ForeignKey(Item, on_delete = models.CASCADE, related_name = 'item4', null = True, default = '')
	quantity4 = models.IntegerField(default = 0, null = True)
	item5 = models.ForeignKey(Item, on_delete = models.CASCADE, related_name = 'item5', null = True, default = '')
	quantity5 = models.IntegerField(default = 0, null = True)
	total = models.IntegerField(default=0)
	ordered = models.IntegerField(default=0)
	num = models.IntegerField(default=0)
	date = models.DateTimeField(auto_now_add = True, null = True)
	
	def __str__(self):
		return str(self.user) + ' - ' + str(self.key)
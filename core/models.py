from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class AccidentDetail(models.Model):
	site = models.CharField(max_length=50)
	date_time = models.DateTimeField()
	cause = models.CharField(max_length=50)
	number_of_vehicle = models.IntegerField()
	people_injured = models.IntegerField()

	def __str__(self):
		return self.site


class UserRoute(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	start = models.CharField(max_length=50)
	destination = models.CharField(max_length=50)
	vehicle = models.CharField(max_length=50)
	number_of_traveller = models.IntegerField()
	landmark1 = models.CharField(max_length=50)
	# landmark2 = models.CharField(max_length=50)

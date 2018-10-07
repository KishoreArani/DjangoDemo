from django.db import models

# Create your models here.
class Distribution_centre(models.Model):
    DC_ID = models.IntegerField(primary_key=True, default=0)
    Contact = models.CharField(max_length=20)
    def __str__(self):
    	return str(self.DC_ID)


class product(models.Model):
	DC_ID = models.ForeignKey(Distribution_centre,on_delete = models.CASCADE)
	P_ID = models.IntegerField(primary_key = True,default = 0)
	NAME = models.CharField(max_length = 50)
	value = models.IntegerField(default = 0)

	def __str__(self):
		return str(self.P_ID)


class Distribution_centre_Address(models.Model):
	zipcode = models.IntegerField(primary_key = True,default = 0)
	city = models.CharField(max_length = 15)
	state = models.CharField(max_length = 15)
	DC_ID = models.ForeignKey(Distribution_centre,on_delete = models.CASCADE)


class Distribution_centre_Location(models.Model):
	DC_ID = models.ForeignKey(Distribution_centre,on_delete = models.CASCADE)
	Xcoordinate = models.FloatField(default = 0)
	Ycoordinate = models.FloatField(default = 0)


class Dealer(models.Model):
	DL_ID = models.IntegerField(primary_key = True,default = 0)
	Contact = models.CharField(max_length = 15)
	DC_ID = models.ForeignKey(Distribution_centre,on_delete = models.CASCADE)

	def __str__(self):
		return str(self.DL_ID)

class Dealer_Address(models.Model):
	zipcode = models.IntegerField(primary_key = True,default = 0)
	city = models.CharField(max_length = 15)
	state = models.CharField(max_length = 15)
	DL_ID = models.ForeignKey(Dealer,on_delete = models.CASCADE)


class Ship(models.Model):
	DC_ID = models.ForeignKey(Distribution_centre,on_delete = models.CASCADE)
	P_ID = models.ForeignKey(product,on_delete = models.CASCADE)
	DL_ID = models.ForeignKey(Dealer,on_delete = models.CASCADE)
	Date = models.DateField()
	Distance = models.IntegerField(default = 0)
	Quantity = models.IntegerField()




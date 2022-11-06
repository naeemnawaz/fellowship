from django.db import models

# Create your models here.
class nearest(models.Model):
	lat = models.FloatField()
	log = models.FloatField()

class away(models.Model):
	lat = models.FloatField()
	log = models.FloatField()
from django.db import models


class Record(models.Model):
	created_at = models.DateTimeField(auto_now_add=True)
	Title = models.CharField(max_length=50)
	Author = models.CharField(max_length=50)
	Booktype = models.CharField(max_length=30)
	Chapters = models.CharField(max_length=30)
	Status =  models.CharField(max_length=100) 
	Genre =  models.CharField(max_length=50)
	Tag =  models.CharField(max_length=100)
	
	def __str__(self):
		return (f"{self.Title}")

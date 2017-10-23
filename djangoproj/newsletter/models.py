from django.db import models

class NewsLetter(models.Model):
	photo_url = models.URLField(null=True)

def __str__(self):
		return self.photo_url
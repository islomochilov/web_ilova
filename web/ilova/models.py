from django.db import models

# Create your models here.

class Yangiliklar(models.Model):
    title = models.CharField(max_length=512)
    content = models.TextField()
    image = models.ImageField(upload_to='images/')
    author = models.CharField(max_length=256)


    def __str__(self):
        return self.title


from email.mime import image
from django.db import models

class Job(models.Model):
    #Bilder und wo wird hochgeladen
    image = models.ImageField(upload_to='images/')

    #Allgemein zu mein arbeit
    summary = models.CharField(max_length=200)

    def __str__(self):
        return self.summary



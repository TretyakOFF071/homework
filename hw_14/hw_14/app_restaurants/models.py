from django.db import models
# Create your models here.

class Restaurant(models.Model):
    name = models.CharField(max_length=30)
    specialization = models.CharField(max_length=20)
    address = models.CharField(max_length=40)
    website = models.URLField(blank=True)
    phone = models.CharField(max_length=12)

    def __str__(self):
        return self.name
from django.db import models

# Create your models here.

class Validation(models.Model):
    data = models.CharField(max_length=200, blank=True, default='')

    def __str__(self):
        return self.data
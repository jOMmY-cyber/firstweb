from django.db import models

class Talking(models.Model):
    name = models.CharField(max_length=10, null=True, blank=True)
    massage = models.CharField(max_length=50, null=True, blank=True)

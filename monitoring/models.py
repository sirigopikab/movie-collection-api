from django.db import models

# Create your models here.
class RequestCount(models.Model):
    key = models.CharField(max_length=50, unique=True)
    count = models.BigIntegerField(default=0)

    def __str__(self):
        return f"{self.key}: {self.count}"
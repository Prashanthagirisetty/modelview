from django.db import models
class function(models.Model):
    name=models.CharField(max_length=20)
    address=models.TextField()
    phone=models.IntegerField()

    def __str__(self):
        return self.name


# Create your models here.

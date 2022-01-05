from django.db import models

class details(models.Model):
    name=models.CharField(max_length=30)
    description=models.TextField(max_length=30)
    costperitem=models.BigIntegerField(null=True)
    stockquantity=models.BigIntegerField(null=True)
    volume=models.BigIntegerField(null=True)

    def __str__(self):
        return self.name
    def get_volume(self):
        volume=self.costperitem*self.stockquantity
        return volume
    def save(self, *args,**kwargs):
        self.volume=self.get_volume()
        super(details,self).save(*args,**kwargs)

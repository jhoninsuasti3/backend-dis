from django.db import models


class Property(models.Model):
    address = models.CharField(max_length=250)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    size = models.IntegerField()
    description = models.TextField()

    def __str__(self):
        return self.address

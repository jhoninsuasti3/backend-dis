from django.db import models

class Property(models.Model):
    PROPERTY_TYPES = (
        ('casa', 'Casa'),
        ('apto', 'Apto'),
    )
    ANTIGUEDAD = (
        ('five_years','menor5'),
        ('five_ten_years','cincoydiez'),        
        ('ten_years','masdediez'),
    )
    address = models.CharField(max_length=250)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    size = models.IntegerField()
    description = models.TextField()
    property_type = models.CharField(
        max_length=5,
        choices=PROPERTY_TYPES,
        default='apto'
    )
    antiguedad = models.CharField(
        max_length=15,
        choices=ANTIGUEDAD,
        default='five_years'
    )
    bedrooms = models.IntegerField(null=True, blank=True)
    bathrooms = models.IntegerField(null=True, blank=True)
    parking_spaces = models.IntegerField(null=True, blank=True)
    year_built = models.IntegerField(null=True, blank=True)
    is_furnished = models.BooleanField(default=False)


    def __str__(self):
        return self.address

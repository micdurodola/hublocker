from django.db import models

# Create your models here.

FEATURED_CHOICES = (
    ('S', 'Small'),
    ('M', 'Medium'),
    ('L', 'Large'),
)

#Locker Model
class Locker(models.Model):  
    specification = models.CharField(max_length=225)
    address=models.CharField(max_length=225)
    city=models.CharField(max_length=225)
    state=models.CharField(max_length=225)
    price=models.CharField(max_length=225)
    first_price=models.CharField(max_length=225)
    quantity = models.IntegerField()
    featured = models.CharField(choices=FEATURED_CHOICES, max_length=1)
    creation_date = models.DateTimeField(auto_now_add=True)

    class meta:
        ordering = ['-creation_date']

    def __str__(self):
        return self.specification

    




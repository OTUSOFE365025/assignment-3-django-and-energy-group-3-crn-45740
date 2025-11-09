import sys

try:
    from django.db import models
except Exception:
    print('Exception: Django Not Found, please install it with "pip install django".')
    sys.exit()

#new Product model for Cash Register Application
class Product(models.Model):
    upc = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    
    def __str__(self):
        return f"{self.name} (${self.price:<.2f})"
    
    def get_rounded_price(self):
        return round(float(self.price), 2)


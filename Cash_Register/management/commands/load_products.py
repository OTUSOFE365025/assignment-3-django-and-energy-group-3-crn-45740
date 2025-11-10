# load_products.py
""" Script to load product data from a text file into the database. """

from django.core.management.base import BaseCommand
from db.models import Product

class Command(BaseCommand):
    help = "Load products from a text file into the database."
    
    def handle(self, *args, **kwargs):
        file_name = "prodInfo.txt"
        with open(file_name, 'r') as file:
            for line in file:
                upc, name, price = line.strip().split()
                Product.objects.update_or_create(
                    upc = int(upc),
                    defaults = {"name": name, "price": float(price)}
                )
        self.stdout.write(self.style.SUCCESS("Products loaded successfully."))
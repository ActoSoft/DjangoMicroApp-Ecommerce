from django.db import models

CATEGORIES = (
    ('electronics', 'Electrónicos'),
    ('cameras', 'Cámaras'),
    ('computers', 'Computadoras'),
    ('cellphones', 'Celulares'),
    ('accesories', 'Accesorios')
)

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=140)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    desc = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='images/products/', blank=True, null=True)
    category = models.CharField(max_length=20, choices=CATEGORIES)
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.name} - ${self.price}'

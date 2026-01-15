from django.db import models

# Create your models here.

class Product(models.Model):
    name=models.CharField(max_length=100)
    description=models.TextField()
    image=models.ImageField(upload_to='product-images/', null=True, blank=True)
    price=models.DecimalField(max_digits=10, decimal_places=2)
    stock=models.PositiveIntegerField(default=0)
    MOQ=models.PositiveIntegerField(default=1)

    def __str__(self):
        return self.name
    
    def is_available(self):
        return self.stock > 0
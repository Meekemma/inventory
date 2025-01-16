from django.db import models
from django.core.validators import MinValueValidator
from django.contrib.auth import get_user_model
User = get_user_model()


class Product(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField()
    quantity = models.PositiveIntegerField(validators=[MinValueValidator(0)])
    price = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0.0)])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    class Meta:
        ordering = ['-created_at', 'name']


    def __str__(self):
        return self.name
    
    
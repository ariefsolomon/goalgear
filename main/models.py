import uuid
from django.db import models

# Create your models here.
class Product(models.Model):
    CATEGORY_CHOICES = [
        ('ball', 'Ball'),
        ('shoes', 'Shoes'),
        ('racket', 'Racket'),
        ('safety', 'Safety'),
    ]
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    description = models.TextField()
    thumbnail = models.URLField()
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='')
    stock = models.IntegerField(default=0)
    brand = models.CharField(max_length=100, blank=True)
    is_featured = models.BooleanField(default=False)

    def __str__(self):
        return self.name
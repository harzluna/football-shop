from django.db import models

# Create your models here.
class Product(models.Model):
    CATEGORY_CHOICES = [
        ('name', 'Name'),
        ('price', 'Price'),
        ('description', 'Description'),
        ('thumbnail', 'thumbnail'),
        ('category', 'Category'),
        ('stock', 'Stock'),
    ]
    
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    description = models.TextField()
    category = models.CharField()
    thumbnail = models.URLField(blank=True, null=True)
    is_featured = models.BooleanField(default=False)

    def __str__(self):
        return self.name
    

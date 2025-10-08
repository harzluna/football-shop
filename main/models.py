from django.db import models
import uuid
from django.contrib.auth.models import User

# Create your models here.
class Product(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    CATEGORY_CHOICES = [
        ('basket', 'Basket'),
        ('football', 'Football'),
        ('badminton', 'Badminton'),
        ('volley', 'Volley'),
        ('baseball', 'Baseball'),
        ('padel', 'Padel'),
        ('tennis', 'Tennis'),
        ('running', 'Running'),
        ('swimming', 'Swimming'),
        ('cycling', 'Cycling'),
        ('fitness', 'Fitness'),
        ('yoga', 'Yoga'),
        ('hiking', 'Hiking'),
        ('climbing', 'Climbing'),
        ('skiing', 'Skiing'),
        ('snowboarding', 'Snowboarding'),
        ('golf', 'Golf'),
        ('fishing', 'Fishing'),
        ('camping', 'Camping'),
        ('other', 'Other'),
    ]
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    description = models.TextField()
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='other')
    thumbnail = models.URLField(blank=True, null=True)
    stock = models.IntegerField(default=0)
    rating = models.FloatField(default=0.0)
    review_count = models.IntegerField(default=0)
    is_featured = models.BooleanField(default=False)

    def __str__(self):
        return self.name
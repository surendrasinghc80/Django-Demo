from django.db import models
from django.utils import timezone

# Create your models here.
class ChaiVarity(models.Model):
    CHAI_TYPE_CHOICES = [
        ('ML', 'Masala Chai'),
        ('GT', 'Green Tea'),
        ('HT', 'Herbal Tea'),
        ('GR', 'Ginger Tea'),
    ]
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='chais/')
    date_added = models.DateTimeField(default=timezone.now)
    type = models.CharField(max_length=2, choices=CHAI_TYPE_CHOICES)
    discription = models.TextField(default="")

    def __str__(self):
        return self.name
    
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

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
    
# One to Many relationship

class ChaiReview(models.Model):
    chai = models.ForeignKey(ChaiVarity, on_delete=models.CASCADE, related_name='reviews')
    user = models.ForeignKey(User, on_delete=models.CASCADE )
    rating = models.IntegerField()
    comment = models.TextField()
    date_added = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.user.username} review for {self.chai.name} - {self.rating}"


# Many to Many relationship
class Store(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=255)
    chai_varities = models.ManyToManyField(ChaiVarity, related_name='stores')
    date_added = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name

# One to One relationship

class ChaiCertificate(models.Model):
    chai = models.OneToOneField(ChaiVarity, on_delete=models.CASCADE, related_name='certificate')
    issue_date = models.DateField()
    valid_until = models.DateField()
    certificate_number = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return f"Certificate for {self.chai.name}"
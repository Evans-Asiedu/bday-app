from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import datetime
from django.utils import timezone



# Create your models here.
class CustomUser(AbstractUser):
    about = models.TextField("About", max_length=10000, blank=True)
    is_doctor = models.BooleanField(default=False)
    image = models.URLField(blank=True, null=True, max_length=500)



class Post(models.Model):
    #list of set 
    CATEGORY = [
        ("Dieting", "Dieting"),
        ("Exercise", "Exercise"),
    ]

    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    title = models.CharField(max_length=80)
    image = models.URLField(blank=True, null=True, max_length=500)
    content = models.CharField(max_length=10000, blank=False, null=False)
    category = models.CharField(choices=CATEGORY, max_length=30)
    publication_date = models.DateTimeField(default=timezone.now())

    def post_date(self):
        return self.publication_date.strftime('%d %B, %Y')
    

    
class Like(models.Model):
    user = models.ForeignKey('CustomUser', on_delete=models.CASCADE)
    post = models.ForeignKey('Post', on_delete=models.CASCADE)



class Appointment(models.Model):
    CATEGORY = [
        ("Medical Examination", "Medical Examination"),
        ("Doctor Check", "Doctor Check"),
        ("Check Up", "Check-Up"),
        ("Result Analysis", "Result Analysis")
    ]

    client = models.ForeignKey('CustomUser', on_delete=models.CASCADE, related_name='client')
    doctor = models.ForeignKey('CustomUser', on_delete=models.CASCADE, related_name='doctor')
    category = models.CharField(choices=CATEGORY, max_length=30)
    appointment_date = models.DateTimeField(default=timezone.now())
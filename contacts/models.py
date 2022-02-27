from django.db import models
from datetime import datetime
# Create your models here.

class Contact(models.Model):
    first_name = models.CharField(max_length=100, blank=True)
    last_name = models.CharField(max_length=100, blank=True)
    customer_need = models.CharField(max_length=100, blank=True)
    city = models.CharField(max_length=100, blank=True)
    state = models.CharField(max_length=100, blank=True)
    email = models.EmailField(max_length=100, blank=True)
    phone = models.CharField(max_length=100, blank=True)
    message = models.TextField(blank=True)
    created_date = models.DateTimeField(blank=True, default=datetime.now)
    
    def __str__(self):
        return self.email
from django.db import models
from django.contrib.auth.models import User



class Blog(models.Model):
    CATEGORY_CHOICES = [
        ('tech', 'Technology'),
        ('life', 'Lifestyle'),
        ('edu', 'Education'),
        ('biz', 'Business'),
        ('news', 'News'),
    ]
    user=models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=1000)
    description = models.CharField(max_length=1000)
    text=models.TextField(max_length=50000, null=True, blank=True)
    category = models.CharField(max_length=100, choices=CATEGORY_CHOICES)
      # Automatically set when created
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    # Automatically updated when object is saved
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)
    def __str__(self):
        return f'{self.title} : {self.description}'


class Comments(models.Model):
    text = models.TextField(max_length=10000)
    blog=models.ForeignKey(Blog, on_delete=models.CASCADE)
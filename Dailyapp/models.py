
# Create your models here.
from email.mime import image
from django.db import models
from distutils.command.upload import upload
from datetime import datetime
from django.forms import DateTimeField
from django.contrib.auth.models import User

# Create your models here.
class Topic(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    title=models.CharField(max_length=200)
    body=models.TextField(blank=True)
    body1=models.TextField(blank=True)
    body2=models.TextField(blank=True)
    body3=models.TextField(blank=True)
    date_created=models.DateTimeField(auto_now_add=True)
    image =models.ImageField(upload_to= 'blog_image' )
    def __str__(self):
        return self.title
    class Meta:
        ordering =['-id']

class Politic(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    title=models.CharField(max_length=200)
    body1=models.TextField(blank=True)
    body2=models.TextField(blank=True)
    body3=models.TextField(blank=True)
    date_created=models.DateTimeField(auto_now_add=True)
    image =models.ImageField(upload_to= 'blog_image' )
    # image2 =models.ImageField(upload_to= 'blog_image' )
    def __str__(self):
        return self.title

    class Meta:
        ordering=['-id']

class New(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    title=models.CharField(max_length=200)
    body1=models.TextField(blank=True)
    body2=models.TextField(blank=True)
    body3=models.TextField(blank=True)
    body=models.TextField(blank=True)
    
    date_created=models.DateTimeField(auto_now_add=True)
    image =models.ImageField(upload_to= 'blog_image' )
    
    def __str__(self):
        return self.title

    class Meta:
        ordering=['-id']

class Metro(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    title=models.CharField(max_length=200)
    
    body=models.TextField(blank=True)
    body1=models.TextField(blank=True)
    body2=models.TextField(blank=True)
    body3=models.TextField(blank=True)
    date_created=models.DateTimeField(auto_now_add=True)
    image =models.ImageField(upload_to= 'blog_image' )
    

    def __str__(self):
        return self.title
    class Meta:
        ordering=['-id']


class Entertainment(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    title=models.CharField(max_length=200)
    
    body=models.TextField(blank=True)
    body1=models.TextField(blank=True)
    body2=models.TextField(blank=True)
    body3=models.TextField(blank=True)
    date_created=models.DateTimeField(auto_now_add=True)
    image =models.ImageField(upload_to= 'blog_image' )
    

    def __str__(self):
        return self.title
    class Meta:
        ordering=['-id']

class latest(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    title=models.CharField(max_length=200)
    
    body=models.TextField(blank=True)
    body1=models.TextField(blank=True)
    body2=models.TextField(blank=True)
    body3=models.TextField(blank=True)
    date_created=models.DateTimeField(auto_now_add=True)
    image =models.ImageField(upload_to= 'blog_image' )
    

    def __str__(self):
        return self.title
    class Meta:
        ordering=['-id']

    

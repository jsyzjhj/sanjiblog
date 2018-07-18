from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
class Category(models.Model):
    name=models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Tag(models.Model):
    name=models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Post(models.Model):
    title= models.CharField(max_length=200)
    body = models.TextField()
    create_time= models.DateTimeField(auto_now_add=True)
    modify_time= models.DateTimeField(auto_now=True)
    excerpt= models.CharField(max_length=200,blank=True)
    tags= models.ManyToManyField(Tag,blank=True)
    category= models.ForeignKey(Category,on_delete=models.DO_NOTHING)
    author= models.ForeignKey(User,on_delete=models.DO_NOTHING)

    def get_absolute_url(self):
        obj=reverse('blog:detail',kwargs={'pk':self.pk})
        return obj

    class Meta:
        ordering = ['-create_time']

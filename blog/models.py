from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
import markdown
from django.utils.html import strip_tags
from comment.models import Comment

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
    cover_pic=models.CharField(max_length=200)
    body = models.TextField()
    create_time= models.DateTimeField(auto_now_add=True)
    modify_time= models.DateTimeField(auto_now=True)
    excerpt= models.TextField(max_length=200,blank=True)
    tags= models.ManyToManyField(Tag,blank=True)
    category= models.ForeignKey(Category,on_delete=models.DO_NOTHING)
    author= models.ForeignKey(User,on_delete=models.DO_NOTHING)
    views = models.PositiveIntegerField(default=0)
    comment_num=models.PositiveIntegerField(default=0)
    likes = models.PositiveIntegerField(default=0)


    def __str__(self):
        return self.title

    def get_absolute_url(self):
        obj=reverse('blog:post',kwargs={'pk':self.pk})
        return obj

    class Meta:
        ordering = ['-create_time']

    def increase_views(self):
        self.views += 1
        self.save(update_fields=['views'])

    def save(self, *args, **kwargs):
        if not self.excerpt:
            md = markdown.Markdown(extensions=[
                'markdown.extensions.extra',
                'markdown.extensions.codehilite',
            ])
            self.excerpt = strip_tags(md.convert(self.body))[:150]
        super(Post, self).save(*args, **kwargs)

class Visitor(models.Model):
    ip = models.GenericIPAddressField()
    user_agent=models.CharField(max_length=200,null=True)
    time = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(Post,on_delete=models.CASCADE)

class Like(Visitor):
    iflike= models.IntegerField(default=0)


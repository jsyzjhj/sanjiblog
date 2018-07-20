from django.db import models
# Create your models here.

class Comment(models.Model):
    #parent_comment=models.ForeignKey('Comment',on_delete=models.DO_NOTHING)
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=255)
    text = models.TextField()
    create_time = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey('blog.Post',on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.text[:20]

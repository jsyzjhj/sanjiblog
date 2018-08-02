from django.db import models
# Create your models here.

class Comment(models.Model):
    ifvalid = models.BooleanField(default=False)
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=255)
    text = models.TextField()
    parent=models.ForeignKey('self',blank=True,null=True,related_name='children',
                                     on_delete=models.SET_NULL)
    create_time = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey('blog.Post',on_delete=models.CASCADE)
    ifparent =models.BooleanField(default=True)
    ip= models.GenericIPAddressField(null=True)
    user_agent=models.CharField(max_length=200,null=True)

    def __str__(self):
        return self.text[:20]
    class Meta():
        ordering=['create_time']

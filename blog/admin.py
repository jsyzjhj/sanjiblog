from django.contrib import admin
from .models import Post,Tag,Category
from comment.models import Comment
# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display=['title','create_time','modify_time','category','author']
class CommentAdmin(admin.ModelAdmin):
    list_display = ['text','name','post','create_time','email']

admin.site.register(Post,PostAdmin)
admin.site.register(Tag)
admin.site.register(Category)
admin.site.register(Comment,CommentAdmin)

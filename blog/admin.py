from django.contrib import admin
from .models import Post,Tag,Category,Visitor,Like,Site
from comment.models import Comment
# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display=['title','create_time','modify_time','category','author']
class CommentAdmin(admin.ModelAdmin):
    list_display = ['text','name','parent','post','create_time','email']

class VisitorAdmin(admin.ModelAdmin):
    list_display = ['ip','post','time','user_agent']

class LikeAdmin(admin.ModelAdmin):
    list_display = ['ip','post','time','user_agent']

admin.site.register(Site)
admin.site.register(Post,PostAdmin)
admin.site.register(Tag)
admin.site.register(Category)
admin.site.register(Comment,CommentAdmin)
admin.site.register(Visitor,VisitorAdmin)
admin.site.register(Like,LikeAdmin)


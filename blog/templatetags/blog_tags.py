from django import template
from ..models import Post,Category,Tag
from django.db.models.aggregates import Count
register = template.Library()

@register.simple_tag
def get_recent_posts(num=5):
    return Post.objects.all().order_by('-create_time')[:num]

@register.simple_tag
def get_archives():
    return Post.objects.dates('create_time', 'month', order='DESC')

@register.simple_tag
def get_categories():
    obj=Category.objects.annotate(num_posts=Count('post')).filter(num_posts__gt=0)
    return obj
@register.simple_tag
def get_tags():
    obj=Tag.objects.annotate(num_posts=Count('post')).filter(num_posts__gt=0)
    return obj
@register.simple_tag
def get_blog_data():
    posts=Post.objects.all()
    total_views=0
    post_num=0
    total_comments=0
    for post in posts:
        comment_list=post.comment_set.all()
        post.comment_num=len(comment_list)
        post_num+=1
        total_views+=post.views
        total_comments+=post.comment_num
    context={
        'post_num':post_num,
        'total_views':total_views,
        'total_comments':total_comments,
    }
    return context

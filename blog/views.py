from django.shortcuts import render,get_object_or_404
from .models import Post
import markdown
# Create your views here.
def index(request):
    posts=Post.objects.all()
    context={
        'posts':posts,
    }
    obj=render(request,'blog/index.html',context=context)
    return obj

def detail(request,pk):
    post=get_object_or_404(Post,pk=pk)
    post.body=markdown.markdown(post.body,
                                extensions=[
                                    'markdown.extensions.extra',
                                    'markdown.extensions.codehilite',
                                    'markdown.extensions.toc',
                                ])
    context={'post':post}
    obj=render(request,'blog/detail.html',context=context)
    return obj



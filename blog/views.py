from django.shortcuts import render,get_object_or_404
from .models import Post,Category
from comment.forms import CommentForm
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
    post.increase_views()
    post.body=markdown.markdown(post.body,
                                extensions=[
                                    'markdown.extensions.extra',
                                    'markdown.extensions.codehilite',
                                    'markdown.extensions.toc',
                                ])
    form=CommentForm()
    comment_list=post.comment_set.all()

    context={'post':post,
             'form':form,
             'comment_list':comment_list}
    obj=render(request,'blog/detail.html',context=context)
    return obj

def archives(request, year, month):
    post_list = Post.objects.filter(create_time__year=year,
                                    create_time__month=month
                                    ).order_by('-create_time')
    obj=render(request, 'blog/index.html', context={'post_list': post_list})
    return obj

def category(request, pk):
    # 记得在开始部分导入 Category 类
    cate = get_object_or_404(Category, pk=pk)
    post_list = Post.objects.filter(category=cate).order_by('-create_time')
    obj=render(request, 'blog/category.html', context={'post_list': post_list})
    return obj




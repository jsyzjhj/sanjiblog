from django.shortcuts import render,get_object_or_404
from .models import Post,Category
from comment.forms import CommentForm
import markdown
# Create your views here.
def index(request):
    posts=Post.objects.all()
    comment_num={}
    for post in posts:
        comment_list=post.comment_set.all()
        post.comment_num=len(comment_list)
    context={
        'posts':posts,
    }
    obj=render(request,'blog/index.html',context=context)
    return obj

def about(request):
    obj=render(request,'blog/about.html')
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
    num_comment=len(comment_list)
    context={'post':post,
             'form':form,
             'comment_list':comment_list,
             'num_comment':num_comment}
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

def mainpage(request):
    posts=Post.objects.all()
    for post in posts:
        comment_list=post.comment_set.all()
        post.comment_num=len(comment_list)
    context={
        'posts':posts,
    }
    obj=render(request, 'forget/mainpage.html', context=context)
    return obj

def post(request,pk):
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
    num_comment=len(comment_list)
    context={'post':post,
             'form':form,
             'comment_list':comment_list,
             'num_comment':num_comment,
            }
    obj=render(request,'forget/post.html',context=context)
    return obj



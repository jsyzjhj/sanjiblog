from django.shortcuts import render,get_object_or_404,redirect
from .models import Post,Category,Visitor,Like
from comment.forms import CommentForm
import markdown
# Create your views here.

def about(request):
    obj=render(request,'blog/about.html')
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
    obj=render(request, 'forget/category.html', context={'post_list': post_list})
    return obj

def mainpage(request):
    posts=Post.objects.all()
    for post in posts:
        comment_list=post.comment_set.all()
        visitors=post.visitor_set.all()
        ips=[]
        for vi in visitors:
            ips.append(vi.ip)
        post.views=len(set(ips))
        post.comment_num=len(comment_list)
        post.save()
    context={
        'posts':posts,
    }
    obj=render(request, 'forget/mainpage.html', context=context)
    return obj

def post(request,pk):
    post = get_object_or_404(Post,pk=pk)
    ip =  request.META['REMOTE_ADDR']
    agent= request.META['HTTP_USER_AGENT']
    visitor=Visitor()
    visitor.ip=ip
    visitor.user_agent=agent
    visitor.post=post
    visitor.save()
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
             'comment_list':comment_list,
            }
    obj=render(request,'forget/post.html',context=context)
    return obj

def like(request,pk):
    ip = request.META['REMOTE_ADDR']
    user_agent= request.META['HTTP_USER_AGENT']
    post=get_object_or_404(Post,pk=pk)
    if Like.objects.filter(ip=ip,post=post,user_agent=user_agent).exists():
        post.likes+=0
        post.save()
        return redirect(post)
    else:
        Like.objects.create(ip=ip,post=post,user_agent=user_agent)
        post.likes+=1
        post.save()
        return redirect(post)

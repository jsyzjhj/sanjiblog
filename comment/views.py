from django.shortcuts import render, get_object_or_404, redirect
from blog.models import Post
from .models import Comment
from .forms import CommentForm

def post_comment(request, post_pk):
    post = get_object_or_404(Post, pk=post_pk)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.ip=request.META['REMOTE_ADDR']
            if comment.parent:
                print('has parent')
                comment.ifparent=False
            comment.save()
            return redirect(post)
        else:
            comment_list = post.comment_set.all()
            comments=[]
            for com in comment_list:
                if com.ifvalid:
                    comments.append(com)
            context = {'post': post,
                       'form': form,
                       'comment_list': comments
                       }
            return render(request, 'forget/post.html', context=context)
    return redirect(post)

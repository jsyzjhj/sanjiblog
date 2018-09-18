from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from blog.models import Post
import json
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
            comment.user_agent=request.META['HTTP_USER_AGENT']
            if comment.parent:
                comment.ifparent = False
            comment.save()

            return HttpResponse('comment')
        else:
            return HttpResponse('invalid')
    else:
        return HttpResponse('not post')

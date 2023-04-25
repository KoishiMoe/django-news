from django.shortcuts import render, redirect
from django.urls import reverse

from comments.models import Comment


# Create your views here.


def comment_add(request, id):
    if not(request.user and request.user.is_authenticated):
        return redirect(reverse('login'))
    Comment.objects.create(content=request.POST.get('content'),
                           author=request.user,
                           post_id=id)
    return redirect(reverse('post_detail', kwargs={'id': id}))

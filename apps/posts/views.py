from django.shortcuts import render, get_object_or_404, redirect

from .models import Post

# Create your views here.


def post_detail(request, id):
    """
    新闻详情
    :param request:
    :param id: 新闻id
    :return:
    """
    post = get_object_or_404(Post, id=id)
    return render(request, 'post.html', context={'post': post})

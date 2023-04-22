from django.contrib.auth.decorators import permission_required
from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.http import require_POST

from posts.models import Post
from .models import Comment

# Create your views here.


@require_POST
@permission_required('comments.add_comment')
def add_comment(request, id):
    """
    添加评论
    :param request:
    :param id: 新闻id
    :return:
    """
    if request.method == 'POST':
        comment = Comment()
        comment.user = request.user
        comment.text = request.POST.get('comment')
        comment.post = get_object_or_404(Post, id=id)
        comment.save()
        return redirect('post_detail', id=id)
    else:
        return redirect('post_detail', id=id)

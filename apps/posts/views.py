from django.core.paginator import PageNotAnInteger, EmptyPage, Paginator
from django.http import Http404
from django.shortcuts import render, get_object_or_404

from comments.models import Comment
from .models import Post, Category


# Create your views here.


def post_detail(request, id):
    """
    新闻详情
    :param request:
    :param id: 新闻id
    :return:
    """
    post = get_object_or_404(Post, id=id)
    if post.approved or request.user.has_perm('posts.view_all_post'):
        comments = Comment.objects.filter(post=post).order_by('-created_time')
        paginator = Paginator(comments, 30)
        page = request.GET.get('page')
        try:
            comments_to_show = paginator.page(page)
        except PageNotAnInteger:
            comments_to_show = paginator.page(1)
        except EmptyPage:
            comments_to_show = paginator.page(paginator.num_pages)
        is_paginated = comments_to_show.has_other_pages()
        return render(request, 'front/post.html', context={'post': post,
                                                           'categories': Category.objects.filter(parent=None),
                                                           'comments': comments_to_show,
                                                           'is_paginated': is_paginated,
                                                           'page_obj': comments_to_show,
                                                           'paginator': paginator
                                                           })
    else:
        raise Http404  # 隐藏未通过审核的新闻id


def category_detail(request, id):
    """
    分类详情
    :param request:
    :param id: 分类id
    :return:
    """
    category = get_object_or_404(Category, id=id)

    posts = Post.objects.filter(category=category, approved=True).order_by('-created_time')
    paginator = Paginator(posts, 10)
    page = request.GET.get('page')
    try:
        posts_to_show = paginator.page(page)
    except PageNotAnInteger:
        posts_to_show = paginator.page(1)
    except EmptyPage:
        posts_to_show = paginator.page(paginator.num_pages)
    is_paginated = True if paginator.num_pages > 1 else False
    return render(request, 'front/category.html', context={'categories': Category.objects.filter(parent=None),
                                                           'category': category,
                                                           'posts': posts_to_show,
                                                           'is_paginated': is_paginated,
                                                           'page_obj': posts_to_show,
                                                           'paginator': paginator})

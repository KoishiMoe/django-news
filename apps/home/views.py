from django.shortcuts import render

from posts.models import Post, Category


# Create your views here.


def home(request):
    # get 21 posts at most to reduce database query
    posts = Post.objects.filter(approved=True).order_by('-created_time')[:25]
    if posts:
        featured_posts = posts[:min(5, len(posts))]
        latest = posts[5:] if len(posts) > 5 else None
        return render(request, 'front/home.html', context={'latest': latest, 'featured_posts': featured_posts,
                                                           'categories': Category.objects.filter(parent=None)})
    else:
        return render(request, 'front/home.html', context={'latest': None, 'featured_posts': None,
                                                           'categories': Category.objects.filter(parent=None)})

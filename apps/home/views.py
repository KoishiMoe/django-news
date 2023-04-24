from django.shortcuts import render

from posts.models import Post, Category


# Create your views here.


def home(request):
    # get 21 posts at most to reduce database query
    posts = Post.objects.filter(approved=True).order_by('-created_time')
    if posts:
        featured_posts = posts.filter(pinned=True)[:min(5, len(posts))]
        if len(featured_posts) < 1:
            featured_posts = posts[:min(5, len(posts))]
        latest = []
        count = 0
        for post in posts:
            if post not in featured_posts and count < 20:
                latest.append(post)
                count += 1
        context = {'latest': latest, 'featured_posts': featured_posts,
                   'categories': Category.objects.filter(parent=None)}
    else:
        context = {'latest': None, 'featured_posts': None,
                   'categories': Category.objects.filter(parent=None)}
    return render(request, 'front/home.html', context=context)


from django.shortcuts import render

from posts.models import Post


# Create your views here.


def home(request):
    # get 21 posts at most to reduce database query
    posts = Post.objects.filter(approved=True).order_by('-created_time')[:21:-1]
    if posts:
        featured = posts[0]
        latest = posts[1:]
        return render(request, 'front/home.html', context={'featured': featured, 'latest': latest})
    else:
        return render(request, 'front/home.html', context={'featured': None, 'latest': None})

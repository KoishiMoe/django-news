from django.shortcuts import render, redirect
from django.contrib import auth

from posts.models import Category
from .forms import RegisterForm, LoginForm
from .models import User


# Create your views here.


def register(request):
    form = RegisterForm()
    categories = Category.objects.filter(parent=None)
    if request.method == 'POST':
        username = request.POST.get('username', '').strip()
        password1 = request.POST.get('password1', '').strip()
        password2 = request.POST.get('password2', '').strip()
        password = password1 if password1 == password2 else None
        email = request.POST.get('email', '').strip()
        if username and password:
            if User.objects.filter(username=username).exists():
                return render(request, 'users/register.html', {'error': '用户名已存在',
                                                               'form': form,
                                                               'categories': categories})
            if email and User.objects.filter(email=email).exists():
                return render(request, 'users/register.html', {'error': '邮箱已存在',
                                                               'form': form,
                                                               'categories': categories})
            user = User.objects.create_user(username=username, password=password, email=email)
            user.is_active = True
            user.save()
            auth.login(request, user)
            return redirect('home')
        else:
            return render(request, 'users/register.html', {'error': '请提供有效的用户名和密码',
                                                           'form': form,
                                                           'categories': categories})
    else:
        return render(request, 'users/register.html', context={
            'form': RegisterForm(),
            'categories': categories
        })


def login(request):
    form = LoginForm()
    categories = Category.objects.filter(parent=None)
    if request.method == 'POST':
        username = request.POST.get('username', '').strip()
        password = request.POST.get('password', '').strip()
        if username and password:
            user = auth.authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    auth.login(request, user)
                    return redirect('home')
                else:
                    return render(request, 'users/login.html', {'error': '用户已被禁用',
                                                                'form': form,
                                                                'categories': categories})
            else:
                return render(request, 'users/login.html', {'error': '用户名或密码错误',
                                                            'form': form,
                                                            'categories': categories})
        else:
            return render(request, 'users/login.html', {'error': '请提供有效的用户名和密码',
                                                        'form': form,
                                                        'categories': categories})
    else:
        return render(request, 'users/login.html', context={
            'form': LoginForm(),
            'categories': categories
        })


def logout(request):
    auth.logout(request)
    return redirect('home')

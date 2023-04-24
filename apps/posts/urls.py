from django.urls import path

from . import views

urlpatterns = [
    path('posts/<int:id>', views.post_detail, name='post_detail'),
    path('category/<int:id>', views.category_detail, name='category_detail'),
    # path('panel/posts/list/', views.post_list, name='news_list'),
    # path('panel/posts/add/', views.post_add, name='news_add'),
    # path('panel/posts/del/<int:pk>/', views.post_delete, name='news_delete'),
    # path('panel/posts/edit/<int:pk>/', views.post_edit, name='news_edit'),
    # path('panel/posts/publish/<int:pk>/', views.post_publish, name='news_publish'),
]


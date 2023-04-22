from django.urls import path

from . import views

urlpatterns = [
    path('', views.panel, name='panel'),
    # path(r'^/panel/news/', views.news, name='news'),
    # path(r'^/panel/news/add/', views.add_news, name='add_news'),
    # path(r'^/panel/news/edit/', views.edit_news, name='edit_news'),
    # path(r'^/panel/news/delete/', views.delete_news, name='delete_news'),
    # path(r'^/panel/news/categories/', views.categories, name='categories'),
    # path(r'^/panel/news/categories/add/', views.add_category, name='add_category'),
    # path(r'^/panel/news/categories/edit/', views.edit_category, name='edit_category'),
    # path(r'^/panel/news/categories/delete/', views.delete_category, name='delete_category'),
    # path(r'^/panel/news/tags/', views.tags, name='tags'),
    # path(r'^/panel/news/tags/add/', views.add_tag, name='add_tag'),
    # path(r'^/panel/news/tags/edit/', views.edit_tag, name='edit_tag'),
    # path(r'^/panel/news/tags/delete/', views.delete_tag, name='delete_tag'),
    # path(r'^/panel/users/', views.users, name='users'),
    # path(r'^/panel/users/add/', views.add_user, name='add_user'),
    # path(r'^/panel/users/edit/', views.edit_user, name='edit_user'),
    # path(r'^/panel/users/delete/', views.delete_user, name='delete_user'),
    # path(r'^/panel/charts/', views.charts, name='charts'),
    # path(r'^/panel/charts/add/', views.add_chart, name='add_chart'),
    # path(r'^/panel/charts/edit/', views.edit_chart, name='edit_chart'),
    # path(r'^/panel/charts/delete/', views.delete_chart, name='delete_chart'),
    # path(r'^/panel/charts/market/', views.market, name='market'),
    # path(r'^/panel/charts/market/add/', views.add_market, name='add_market'),
    # path(r'^/panel/charts/market/edit/', views.edit_market, name='edit_market'),
    # path(r'^/panel/charts/market/delete/', views.delete_market, name='delete_market'),
]

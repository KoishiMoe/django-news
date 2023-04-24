from django.urls import path

from . import views


urlpatterns = [
    path('add/<int:id>', views.comment_add, name='comment_add'),
]

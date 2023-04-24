from django.contrib import admin

# Register your models here.


from .models import Comment


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    class Meta:
        verbose_name = '评论'
        verbose_name_plural = '评论'
    list_display = ('id', 'author', 'post', 'content', 'created_time')
    search_fields = ('content', 'author__username', 'author__display_name', 'post__title')
    list_filter = ('created_time',)

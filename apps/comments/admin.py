from django.contrib import admin

# Register your models here.


from .models import Comment


class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'post', 'text', 'created_time')
    list_filter = ('created_time', 'user')
    search_fields = ('text', 'user')


admin.site.register(Comment, CommentAdmin)

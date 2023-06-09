from django.contrib import admin
from django.contrib.auth.decorators import permission_required

# from django_summernote.admin import SummernoteModelAdmin

# Register your models here.


from .models import Post, Category  # , Tag


class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'author', 'created_time', 'approved')
    list_filter = ('approved', 'created_time', 'category')
    search_fields = ('title', 'body', 'author__username', 'author__display_name')
    actions = ['approve_posts']
    # exclude = ('comments',)
    # summernote_fields = ('body',)

    @permission_required('posts.approve_post')
    def approve_posts(self, request, queryset):
        if queryset.update(approved=True) == 1:
            message_bit = '通过了1篇文章'
        else:
            message_bit = '通过了%s篇文章' % queryset.count()
        self.message_user(request, '%s' % message_bit)

    approve_posts.short_description = '通过选中的 文章'

    @permission_required('posts.pin_post')
    def pin_post(self, request, queryset):
        if queryset.update(pinned=True) == 1:
            message_bit = '置顶了1篇新闻'
        else:
            message_bit = '置顶了%s篇新闻' % queryset.count()
        self.message_user(request, '%s' % message_bit)

    def save_model(self, request, obj, form, change):
        if not request.user.has_perm('posts.approve_post'):
            obj.approved = False
        try:
            obj.author
        except AttributeError:
            obj.author = request.user
        if not request.user.has_perm('posts.change_author'):
            obj.author = request.user
        super().save_model(request, obj, form, change)


admin.site.register(Post, PostAdmin)
admin.site.register(Category)
# admin.site.register(Tag)

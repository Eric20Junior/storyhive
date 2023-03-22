from django.contrib import admin
from .models import Post, Category, Comment

# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'status', 'publish_date', 'published')
    list_filter = ('status',)
    search_fields = ['title']
    prepopulated_fields = {'slug': ('title',)}

class CommentAdmin(admin.ModelAdmin):
    list_display = ('post', 'user', 'content', 'created_on')

admin.site.register(Post, PostAdmin)
admin.site.register(Category)
admin.site.register(Comment)
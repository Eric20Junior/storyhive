from django.contrib import admin
from .models import Post, Category

# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'status', 'publish_date', 'published')
    list_filter = ('status',)
    search_fields = ['title']
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(Post, PostAdmin)
admin.site.register(Category)
from django.contrib import admin
from .models import BlogPost


class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('author', 'title', 'content', 'created_date', 'updated_date')
    list_filter = ("author",)


admin.site.register(BlogPost, BlogPostAdmin)

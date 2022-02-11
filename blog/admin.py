from django.contrib import admin
from .models import Post


class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'author', 'title', 'created_date', 'published_date')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'text')
    list_editable = ('published_date',)
    list_filter = ('published_date', 'id',)


admin.site.register(Post, PostAdmin)

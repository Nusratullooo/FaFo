from django.contrib import admin
from news.models import News, Comment_news


class NewsAdmin(admin.ModelAdmin):
    list_display = ['title', 'name',  'image_tag', 'create_at']
    readonly_fields = ('image_tag',)


class Comment_newsAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'comment']
    list_filter = ['status']
    readonly_fields = ('name', 'email', 'comment', 'ip', 'news')


admin.site.register(Comment_news, Comment_newsAdmin)
admin.site.register(News, NewsAdmin)

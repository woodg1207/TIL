from django.contrib import admin
from .models import Article, Comment
# Register your models here.
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title', 'content',)

admin.site.register(Article, ArticleAdmin)

class Commentadmin(admin.ModelAdmin):
    list_display = ('pk', 'content',)

admin.site.register(Comment, Commentadmin)
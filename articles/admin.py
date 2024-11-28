from django.contrib import admin

from articles.models import Article


# Register your models here.

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'date', 'body')
    save_as = True


admin.site.register(Article, ArticleAdmin)

from django.contrib import admin

from .models import Profile, News, Article, Statement, NewsComment, ArticleComment


admin.site.register(Profile)
admin.site.register(News)
admin.site.register(Article)
admin.site.register(Statement)
admin.site.register(NewsComment)
admin.site.register(ArticleComment)

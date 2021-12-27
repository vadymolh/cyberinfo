from django.contrib import admin
from django.urls import path, re_path
from . import views

from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('',views.showMain),
    path('register/', views.register),
    path('logout/', views.logout_user, name='logout'),
    path('login/', views.login_user, name='login'),
    path('main/', views.showMain),

    path('profile/', views.profile),
    path('profile/<int:user_id>/', views.another_profile,  name='another_profile'),
    path('profile/upgrade/', views.upgrade_profile),

    path('news/<int:news_id>/',views.show_one_news,  name='one_news'),
    path('news/add/', views.add_news),
    path('news/edit/<int:news_id>/', views.edit_news,  name='edit_one_news'),
    path('news/delete/<int:news_id>/',views.delete_news,  name='news_delete'),
    path('news/delete/comment/<int:news_id>/<int:comment_id>',views.delete_news_comment,  name='news_comment_delete'),
    path('news/edit/comment/<int:news_id>/<int:comment_id>',views.edit_news_comment,  name='news_comment_edit'),
    re_path(r'^news*',views.show_news),

    path('article/add/', views.add_article),
    path('article/edit/<int:article_id>/', views.edit_article,  name='edit_one_article'),
    path('article/<int:article_id>/',views.show_one_article,  name='one_article'),
    path('article/delete/<int:article_id>/',views.delete_article,  name='article_delete'),
    path('article/delete/comment/<int:article_id>/<int:comment_id>',views.delete_article_comment,  name='article_comment_delete'),
    path('article/edit/comment/<int:article_id>/<int:comment_id>',views.edit_article_comment,  name='article_comment_edit'),
    re_path(r'^articles*',views.show_articles),

    path('ourarticles/',views.show_ourarticles),
    path('ourarticles/cybersecurity/',views.cybersecurity),
    path('ourarticles/authentication/',views.multi_factor_authentication),
    path('ourarticles/virus/',views.computer_virus),
    path('ourarticles/facebook/',views.facebook_fallendown),
    path('ourarticles/password/generate/<str:password>', views.passwordGenerate, name='password_generate'),
    path('ourarticles/password/', views.password),

    path('change_theme/<str:theme_name>', views.change_theme, name='change_theme'),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

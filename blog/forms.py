# -*- coding: utf-8 -*-
from django import forms
from .models import Profile, News, Article, Statement, NewsComment, ArticleComment, StatementComment
from django.contrib.auth.models import User


class NewsCommentForm(forms.ModelForm):
    class Meta:
        model = NewsComment
        fields = ('body',)

class ArticleCommentForm(forms.ModelForm):
    class Meta:
        model = ArticleComment
        fields = ('body',)


class Add_newsForm(forms.ModelForm):
    class Meta:
        model = News
        fields = ('image', 'title', 'text',)

class DeleteNewsForm(forms.ModelForm):
    class Meta:
        model = News
        fields = []


class DeleteArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = []

class EditNewsCommentForm(forms.ModelForm):
    class Meta:
        model = NewsComment
        fields = ('body',)


class DeleteNewsCommentForm(forms.ModelForm):
    class Meta:
        model = NewsComment
        fields = []

class StatementCommentForm(forms.ModelForm):
    class Meta:
        model = StatementComment
        fields = ('body',)

class EditStatementCommentForm(forms.ModelForm):
    class Meta:
        model = StatementComment
        fields = ('body',)


class DeleteStatementCommentForm(forms.ModelForm):
    class Meta:
        model = StatementComment
        fields = []

class AddArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ('image', 'title', 'text',)


class EditArticleCommentForm(forms.ModelForm):
    class Meta:
        model = NewsComment
        fields = ('body',)


class DeleteArticleCommentForm(forms.ModelForm):
    class Meta:
        model = NewsComment
        fields = []



class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username',)




class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile

        fields = ('user_image', 'info',)


class ChangeProfileRoleForm(forms.ModelForm):
    class Meta:
        model = Profile

        fields = ('role',)



class AddStatementForm(forms.ModelForm):
    class Meta:
        model = Statement
        fields = (
            'title',
            'image1',
            'image2',
            'image3',
            'description',
            'public',
        )

class EditStatementForm(forms.ModelForm):
    class Meta:
        model = Statement
        fields = (
            'title',
            'image1',
            'image2',
            'image3',
            'description',
            'public',
        )

class DeleteStatementForm(forms.ModelForm):
    class Meta:
        model = Statement
        fields = []

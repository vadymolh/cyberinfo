from django.shortcuts import render, get_object_or_404, redirect
from .models import (
    News,
    Article,
    Profile,
    NewsComment,
    ArticleComment,
)
from .forms import (
    Password,
    UserForm,
    ProfileForm,
    ChangeProfileRoleForm,
    Add_newsForm,
    AddArticleForm,
    NewsCommentForm,
    ArticleCommentForm,
    DeleteNewsCommentForm,
    EditNewsCommentForm,
    DeleteArticleCommentForm,
    EditArticleCommentForm,
    DeleteNewsForm,
    DeleteArticleForm,
)

from django.core.paginator import Paginator
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm
from PIL import Image
from django.http import JsonResponse
import json
import requests
import random




def get_style(request):
    if('theme' in request.COOKIES):
        file = request.COOKIES['theme']
    else:
        file = 'css/dark_theme.css'
    return(file)


def get_info(request):
    islogin = request.user.is_authenticated
    style_file = get_style(request)
    return(islogin, style_file)























def showMain(request):
    islogin, style_file = get_info(request)

    res = News.objects.all()
    res = res.filter(active=True)
    res = list(reversed(res))
    news = res[0]

    res = Article.objects.all()
    res = res.filter(active=True)
    res = list(reversed(res))
    article = res[0]

    context = {

           'islogin': islogin,
           'style_file': style_file,
           'news': news,
           'article': article,
          }
    return render(request, 'index.html', context)  # render main page



def register(request):
    islogin, style_file = get_info(request)
    err = ''
    if(request.method == "POST"):
        user_form = UserCreationForm(request.POST)
        if user_form.is_valid():
            user = user_form.save()
            login(request, user)
            return redirect("/main")
        else:
            err = user_form.errors.as_data()
    else:
        user_form = UserCreationForm()

    err = str(err).split("'")
    error = []
    for i in err:
        res = i.split(".")
        for ii in res:
            if ii == '':
                error.append(i)

    context = {

        'error': error,
        'islogin': islogin,
        'user_form': user_form,
        'style_file': style_file
    }
    return render(request, 'primitive/register_page.html', context)


def logout_user(request):
    logout(request)
    return redirect("/main")


def login_user(request):
    islogin, style_file = get_info(request)
    err = ''
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('/main')
            else:
                err = "Користувач з таким імям вже існує"
        else:
            err = "Не правильно вказаний логін чи пароль"

    form = AuthenticationForm()
    context = {

        'error': err,
        'islogin': islogin,
        'form': form,
        'style_file': style_file
    }

    return render(request, 'primitive/login_page.html', context)





def show_ourarticles(request):
    islogin, style_file = get_info(request)
    context = {
        'islogin': islogin,
        'style_file': style_file,
    }
    return render(request, 'ourarticle/ourarticle_page.html', context)

def cybersecurity(request):
    islogin, style_file = get_info(request)
    context = {
        'islogin': islogin,
        'style_file': style_file,
    }
    return render(request, 'ourarticle/cybersecurity.html', context)

def multi_factor_authentication(request):
    islogin, style_file = get_info(request)

    context = {
        'islogin': islogin,
        'style_file': style_file,
    }
    return render(request, 'ourarticle/multi_factor_authentication_page.html', context)

def facebook_fallendown(request):
    islogin, style_file = get_info(request)

    context = {
        'islogin': islogin,
        'style_file': style_file,
    }
    return render(request, 'ourarticle/facebook_fallendown.html', context)


def computer_virus(request):
    islogin, style_file = get_info(request)

    context = {
        'islogin': islogin,
        'style_file': style_file,
    }
    return render(request, 'ourarticle/computer_virus.html', context)


def passwordGenerate(request, password):
    islogin, style_file = get_info(request)
    length = 0
    chars = ""
    row_len = 100

    chars_variant = {
        "numbers": "1234567890",
        "letters": "abcdefghijklmnopqrstuvwxyz",
        "bigletters": "ABCDEFGHIJKLMNOPQRSTUVWXYZ",
        "another": "+-*!&$=@<>",
        "": "",
    }

    time = ""

    if request.method == 'POST':
        form = Password(data=request.POST)
        length = request.POST['length']
        try:
            numbers = request.POST['numbers']
        except:
            numbers = ""
        try:
            letters = request.POST['letters']
        except:
            letters = ""
        try:
            bigletters = request.POST['bigletters']
        except:
            bigletters = ""
        try:
            another = request.POST['another']
        except:
            another = ""
        chars = chars_variant[numbers] + chars_variant[letters] + chars_variant[bigletters] + chars_variant[another]
        password = ""
        for i in range(int(length)):
            password += list(chars)[random.randint(0, len(chars))-1]

        symbols_amount = len(chars)
        speed = request.POST['speed']

        time_in_second = pow(int(symbols_amount), int(length)) // int(speed)

        time_in_minute = int(time_in_second // 60)
        time_in_hour = int(time_in_minute // 60)
        time_in_day = int(time_in_hour // 24)
        time_in_year = int(time_in_day // 365)

        time = [time_in_second, time_in_minute, time_in_hour, time_in_day, time_in_year]
        for i in range(time.count(0)):
            time.remove(0)
        time = str(min(time))

        univarse_life = int(13.799 * (10**9))

        if int(time) >= univarse_life:
            time = "Це займе більше часу чим вік всесвіту"
        elif int(time) == time_in_year:
            time = str(time) + " роки"
        elif int(time) == time_in_day:
            time = str(time) + " днів"
        elif int(time) == time_in_hour:
            time = str(time) + " годин"
        elif int(time) == time_in_minute:
            time = str(time) + " хвилин"
        elif int(time) == time_in_second:
            time = str(time) + " секунд"

    else:
        form = Password()

        password = reversed([password[0:len(password)%row_len]] + [password[i:i+row_len] for i in range(len(password)%row_len, len(password), row_len)])



    context = {
        'islogin': islogin,
        'style_file': style_file,
        'password': password,
        'form': form,
        'time': time,
        }
    return render(request, 'ourarticle/password.html', context)

def password(request):
    islogin, style_file = get_info(request)
    password = "0"

    chars_variant = {
        "numbers": "1234567890",
        "letters": "abcdefghijklmnopqrstuvwxyz",
        "bigletters": "ABCDEFGHIJKLMNOPQRSTUVWXYZ",
        "another": "+-*!&$=@<>",
        "": "",
    }

    if request.method == 'POST':
        form = Password(data=request.POST)
        length = request.POST['length']
        try:
            numbers = request.POST['numbers']
        except:
            numbers = ""
        try:
            letters = request.POST['letters']
        except:
            letters = ""
        try:
            bigletters = request.POST['bigletters']
        except:
            bigletters = ""
        try:
            another = request.POST['another']
        except:
            another = ""
        chars = chars_variant[numbers] + chars_variant[letters] + chars_variant[bigletters] + chars_variant[another]
        password = ""
        for i in range(int(length)):
            password += list(chars)[random.randint(0, len(chars))-1]
        return redirect(f"/ourarticles/password/generate/{password}#gen")
    else:
        form = Password()

    context = {
        'islogin': islogin,
        'style_file': style_file,
        'password': password,
        'form': form,
        }
    return render(request, 'ourarticle/password.html', context)


def showPasswordGenerator(request):
    islogin, style_file = get_info(request)
    password = "0"
    context = {
        'islogin': islogin,
        'style_file': style_file,
        'password': password,
    } # page context
    return render(request, 'ourarticle/password.html', context) # render password page













def show_news(request):
    islogin = request.user.is_authenticated  # залогинен ли вользователь
    style_file = get_style(request)  # узнаём какая тема

    res = News.objects.all()
    res = res.filter(active=True)
    res = list(reversed(res))
    paginator = Paginator(res, 3)
    page_num = request.GET.get('page')
    news = paginator.get_page(page_num)

    context = {
        'newses': news,
        'paginator': paginator,
        'islogin': islogin,

        'style_file': style_file
    }
    return render(request, 'news/news_page.html', context)


def show_one_news(request, news_id):
    islogin, style_file = get_info(request)
    res = get_object_or_404(News, pk=news_id)
    news_text = res.text.split("\r\n")
    user = request.user.username

    comments = res.comments.filter(active=True)
    if request.method == 'POST':
        comment_form = NewsCommentForm(data=request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.name = request.user.username
            new_comment.role = request.user.profile.role
            new_comment.image = request.user.profile.user_image.url
            new_comment.userid = request.user.pk
            new_comment.news = res
            new_comment.save()
            return redirect(f"/news/{news_id}/")
    else:
        comment_form = NewsCommentForm()

    context = {
        'news': res,
        'islogin': islogin,
        'news_text': news_text,
        'user': user,
        'comments': comments,
        'comment_form': comment_form,

        'style_file': style_file
    }
    return render(request, 'news/one_news_page.html', context)


def delete_news_comment(request, comment_id, news_id):
    islogin, style_file = get_info(request)
    comment_to_delete = get_object_or_404(NewsComment, id=comment_id)
    name = comment_to_delete.name
    if request.method == 'POST':
        form = DeleteNewsCommentForm(request.POST, instance=comment_to_delete)

        if form.is_valid():
            comment_to_delete.delete()
            return redirect(f"/news/{news_id}/")

    else:
        form = DeleteNewsCommentForm(instance=comment_to_delete)

    context = {
        'islogin': islogin,
        'form': form,
        'name': name,

        'style_file': style_file
    }
    return render(request, 'news/delete_news_comment_page.html', context)

def delete_news(request, news_id):
    islogin, style_file = get_info(request)
    news_to_delete = get_object_or_404(News, id=news_id)
    name = news_to_delete.author
    if request.method == 'POST':
        form = DeleteNewsForm(request.POST, instance=news_to_delete)

        if form.is_valid():
            news_to_delete.delete()
            return redirect(f"/news/")

    else:
        form = DeleteNewsForm(instance=news_to_delete)

    context = {
        'islogin': islogin,
        'form': form,
        'name': name,

        'style_file': style_file
    }
    return render(request, 'news/delete_news_page.html', context)



def edit_news_comment(request, comment_id, news_id):
    islogin, style_file = get_info(request)
    res = get_object_or_404(News, pk=news_id)
    news_text = res.text.split("\r\n")
    user = request.user.username

    comments = res.comments.filter(active=True)

    comment_to_edit = get_object_or_404(NewsComment, id=comment_id)
    if request.method == 'POST':
        edit_comment_form = EditNewsCommentForm(
            request.POST,
            instance=comment_to_edit
        )
        if edit_comment_form.is_valid():
            edit_comment_form.save()
            return redirect(f"/news/{news_id}/")
        else:
            err = edit_comment_form.errors.as_data()
            print(err)
    else:
        comment_form = NewsCommentForm()
        edit_comment_form = EditNewsCommentForm(instance=comment_to_edit)

    context = {
        'news': res,
        'islogin': islogin,
        'news_text': news_text,
        'user': user,
        'comments': comments,
        'comment_form': comment_form,
        'edit_comment_form': edit_comment_form,
        'comment_id': comment_id,

        'style_file': style_file
    }
    return render(request, 'news/edit_news_comment_page.html', context)


def add_news(request):
    islogin, style_file = get_info(request)

    if(request.method == "POST"):
        news_form = Add_newsForm(request.POST, request.FILES)
        if(news_form.is_valid()):
            new = news_form.save(commit=False)
            new.author = request.user.username
            new.save()
            news_form.save()
            return redirect("/news")
    else:
        news_form = Add_newsForm()

    role = request.user.profile.role

    context = {

        'islogin': islogin,
        'news_form': news_form,
        'role': role,

        'style_file': style_file
    }
    return render(request, 'news/add_news_page.html', context)


def edit_news(request, news_id):
    islogin, style_file = get_info(request)
    res = get_object_or_404(News, pk=news_id)

    if(request.method == "POST"):
        news_form = Add_newsForm(request.POST, request.FILES, instance=res)
        if news_form.is_valid():
            news_form.save()
            return redirect("/news")
    else:
        news_form = Add_newsForm(instance=res)

    author = res.author
    user = request.user
    image = res.image.url

    context = {

        'islogin': islogin,
        'news_form': news_form,
        'author': author,
        'user': user,
        'image': image,

        'style_file': style_file
    }
    return render(request, 'news/edit_news_page.html', context)











def show_articles(request):
    islogin, style_file = get_info(request)

    res = Article.objects.all()
    res = res.filter(active=True)
    res = list(reversed(res))
    paginator = Paginator(res, 6)
    page_num = request.GET.get('page')
    article = paginator.get_page(page_num)


    context = {
        'articles': article,
        'paginator': paginator,
        'islogin': islogin,
        'style_file': style_file
    }
    return render(request, 'article/article_page.html', context)


def show_one_article(request, article_id):
    islogin, style_file = get_info(request)
    res = get_object_or_404(Article, pk=article_id)
    article_text = res.text.split("\r\n")
    user = request.user.username

    comments = res.comments.filter(active=True)
    comments = reversed(comments)
    if request.method == 'POST':
        comment_form = ArticleCommentForm(data=request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.name = request.user.username
            new_comment.role = request.user.profile.role
            new_comment.image = request.user.profile.user_image.url
            new_comment.userid = request.user.pk
            new_comment.article = res
            new_comment.save()
            return redirect(f"/article/{article_id}/")
    else:
        comment_form = ArticleCommentForm()

    context = {
        'article': res,
        'islogin': islogin,
        'article_text': article_text,
        'user': user,
        'comments': comments,
        'comment_form': comment_form,
        'style_file': style_file
    }
    return render(request, 'article/one_article_page.html', context)


def delete_article(request, article_id):
    islogin, style_file = get_info(request)
    article_to_delete = get_object_or_404(Article, id=article_id)
    name = article_to_delete.author
    if request.method == 'POST':
        form = DeleteArticleForm(request.POST, instance=article_to_delete)

        if form.is_valid():
            article_to_delete.delete()
            return redirect(f"/articles/")

    else:
        form = DeleteArticleForm(instance=article_to_delete)

    context = {
        'islogin': islogin,
        'form': form,
        'name': name,
        'style_file': style_file
    }
    return render(request, 'article/delete_article_page.html', context)



def delete_article_comment(request, comment_id, article_id):
    islogin, style_file = get_info(request)
    comment_to_delete = get_object_or_404(ArticleComment, id=comment_id)
    name = comment_to_delete.name
    if request.method == 'POST':
        form = DeleteArticleCommentForm(request.POST, instance=comment_to_delete)

        if form.is_valid():
            comment_to_delete.delete()
            return redirect(f"/article/{article_id}/")

    else:
        form = DeleteArticleCommentForm(instance=comment_to_delete)

    context = {
        'islogin': islogin,
        'form': form,
        'name': name,
        'style_file': style_file
    }
    return render(request, 'article/delete_article_comment_page.html', context)


def edit_article_comment(request, comment_id, article_id):
    islogin, style_file = get_info(request)
    res = get_object_or_404(Article, pk=article_id)
    article_text = res.text.split("\r\n")
    user = request.user.username

    comments = res.comments.filter(active=True)
    comments = reversed(comments)
    comment_to_edit = get_object_or_404(ArticleComment, id=comment_id)
    if request.method == 'POST':
        edit_comment_form = EditArticleCommentForm(
            request.POST,
            instance=comment_to_edit
        )
        if edit_comment_form.is_valid():
            edit_comment_form.save()
            return redirect(f"/article/{article_id}/")
        else:
            err = edit_comment_form.errors.as_data()
    else:
        comment_form = ArticleCommentForm()
        edit_comment_form = EditArticleCommentForm(instance=comment_to_edit)

    context = {
        'article': res,
        'islogin': islogin,
        'article_text': article_text,
        'user': user,
        'comments': comments,
        'comment_form': comment_form,
        'edit_comment_form': edit_comment_form,
        'comment_id': comment_id,
        'style_file': style_file
    }
    return render(request, 'article/edit_article_comment_page.html', context)


def add_article(request):
    islogin, style_file = get_info(request)

    if(request.method == "POST"):
        article_form = AddArticleForm(request.POST, request.FILES)
        if(article_form.is_valid()):
            article = article_form.save(commit=False)
            article.author = request.user.username
            article.save()
            article_form.save()
            return redirect("/article")
    else:
        article_form = AddArticleForm()

    role = request.user.profile.role

    context = {

        'islogin': islogin,
        'article_form': article_form,
        'role': role,
        'style_file': style_file
    }
    return render(request, 'article/add_article_page.html', context)


def edit_article(request, article_id):
    islogin, style_file = get_info(request)
    res = get_object_or_404(Article, pk=article_id)

    if(request.method == "POST"):
        article_form = AddArticleForm(request.POST, request.FILES, instance=res)
        if article_form.is_valid():
            article_form.save()
            return redirect("/article")
    else:
        article_form = AddArticleForm(instance=res)

    author = res.author
    user = request.user
    image = res.image.url

    context = {

        'islogin': islogin,
        'article_form': article_form,
        'author': author,
        'user': user,
        'image': image,
        'style_file': style_file
    }
    return render(request, 'article/edit_article_page.html', context)



def upgrade_profile(request):
    islogin, style_file = get_info(request)
    err = ''
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = ProfileForm(
            request.POST,
            request.FILES,
            instance=request.user.profile
        )
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()

            profile_form.save()
            return redirect('/profile')
        else:
            err = user_form.errors.as_data()
    else:
        user_form = UserForm(instance=request.user)
        profile_form = ProfileForm(instance=request.user.profile)
        err = user_form.errors.as_data()

    err = str(err).split("'")
    error = []
    for i in err:
        res = i.split(".")
        for ii in res:
            if ii == '':
                error.append(i)

    user_image = request.user.profile.user_image.url

    context = {

        'user_image': user_image,
        'islogin': islogin,
        'user_form': user_form,
        'profile_form': profile_form,
        'error': error,

        'style_file': style_file
    }
    return render(request, 'profile/upgrade_profile_page.html', context)


def profile(request):
    islogin, style_file = get_info(request)

    username = request.user.username
    user_image = request.user.profile.user_image.path
    full_info = request.user.profile.info.split("\r\n")
    role = request.user.profile.role
    admin = request.user.profile.admin
    userid = request.user.pk

    if username != 'Kikono':
        user_image = user_image.replace("\\", "/")
        img = Image.open(user_image)
        width = img.size[0]
        height = img.size[1]
        if width != height:
            newsize = (width, width)
            img = img.resize(newsize)
            width = img.size[0]
            height = img.size[1]
            img.save(user_image, format="png")

    user_image = request.user.profile.user_image.url

    if 'Журналист' in role:
        role_color = "rgb(0, 200, 100)"
    elif style_file == 'css/light.css' or style_file == 'css/purple_gold.css':
        role_color = "black"
    else:
        role_color = "black"

    context = {

        'islogin': islogin,
        'user_image': user_image,
        'username': username,
        'full_info': full_info,
        'role': role,
        'admin': admin,
        'userid': userid,
        'role_color': role_color,

        'style_file': style_file
    }
    return render(request, 'profile/profile_page.html', context)


def another_profile(request, user_id):
    islogin, style_file = get_info(request)

    user = get_object_or_404(User, pk=user_id)

    username = user.username
    user_image = user.profile.user_image.url
    full_info = user.profile.info.split("\r\n")
    role = user.profile.role
    admin = user.profile.admin


    if 'Журналист' in role:
        role_color = "rgb(0, 200, 100)"
    elif style_file == 'css/light.css' or style_file == 'css/purple_gold.css':
        role_color = "black"
    else:
        role_color = "black"

    if request.method == 'POST':
        profile_form = ChangeProfileRoleForm(request.POST, instance=user.profile)
        if profile_form.is_valid():
            profile_form.save()
            return redirect(f"/profile/{user_id}/")
        else:
            pass

    else:
        profile_form = ChangeProfileRoleForm(instance=user.profile)


    context = {

        'islogin': islogin,
        'user_image': user_image,
        'username': username,
        'full_info': full_info,
        'role': role,
        'admin': admin,
        'profile_form': profile_form,
        'user': user,
        'role_color': role_color,

        'style_file': style_file
    }

    return render(request, 'profile/another_profile_page.html', context)










def change_theme(request, theme_name):
    style_file = f'css/{theme_name}.css'
    response = redirect("/main")
    response.set_cookie('theme', style_file)
    return response

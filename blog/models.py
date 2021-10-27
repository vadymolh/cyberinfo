from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from multiselectfield import MultiSelectField

class News(models.Model):
    image = models.ImageField(
        upload_to='news/image/',
        height_field=None,
        width_field=None,
        max_length=100
    )
    title = models.CharField(max_length=1000)
    text = models.TextField()
    create_date = models.DateTimeField(default=timezone.now)
    pyblished_date = models.DateTimeField(null=True, blank=True)
    active = models.BooleanField(default=True)
    author = models.CharField(max_length=100, default="ananist")

    def publish(self):
        self.publish_date = timezone.now()


class NewsComment(models.Model):
    news = models.ForeignKey(
        News, related_name='comments', on_delete=models.CASCADE
    )
    image = models.CharField(max_length=300, default="none")
    name = models.CharField(max_length=100)
    userid = models.CharField(max_length=1000, default=3)
    role = models.CharField(max_length=100, default="Игрок")
    body = models.TextField()
    created = models.DateTimeField(default=timezone.now)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ('created',)


class Article(models.Model):
    image = models.ImageField(
        upload_to='article/image/',
        height_field=None,
        width_field=None,
        max_length=100
    )
    title = models.CharField(max_length=1000)
    text = models.TextField()
    create_date = models.DateTimeField(default=timezone.now)
    active = models.BooleanField(default=True)
    author = models.CharField(max_length=100, default="ananist")



class ArticleComment(models.Model):
    article = models.ForeignKey(
        Article, related_name='comments', on_delete=models.CASCADE
    )
    image = models.CharField(max_length=300, default="none")
    name = models.CharField(max_length=100)
    userid = models.CharField(max_length=1000, default=3)
    role = models.CharField(max_length=100, default="Игрок")
    body = models.TextField()
    created = models.DateTimeField(default=timezone.now)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ('created',)

class Profile(models.Model):
    role1 = 'Користувач'
    role2 = 'Журналист'
    ROLES = [
        (role1, 'Користувач'),
        (role2, 'Журналист'),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    user_image = models.ImageField(
        upload_to='users/user_image/',
        default="users/user_image/default/default.png",
        blank=True
    )

    info = models.TextField(
        default='Проходивший мимо пользователь сайта,'
        'который ничего о себе не написал',
        max_length=1000
    )

    create_date = models.DateTimeField(default=timezone.now)
    role = MultiSelectField(choices=ROLES, default=role1)
    admin = models.BooleanField(default=False)


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()


class Statement(models.Model):
    title = models.CharField(max_length=1000, default="Не описано.")
    site_username = models.CharField(max_length=100, default="Не указано")

    image1 = models.ImageField(
        default="statement/image/default/default.png",
        upload_to='statement/image/',
        max_length=100,
        blank=True
    )
    image2 = models.ImageField(
        default="statement/image/default/default.png",
        upload_to='statement/image/',
        max_length=100,
        blank=True
    )

    image3 = models.ImageField(
        default="statement/image/default/default.png",
        upload_to='statement/image/',
        max_length=100,
        blank=True
    )

    description = models.TextField(default="Не описано.")
    public = models.BooleanField(default=False)
    create_date = models.DateTimeField(default=timezone.now)

class StatementComment(models.Model):
    statement = models.ForeignKey(
        Statement, related_name='comments', on_delete=models.CASCADE
    )
    image = models.CharField(max_length=300, default="none")
    name = models.CharField(max_length=100)
    userid = models.CharField(max_length=1000, default=3)
    role = models.CharField(max_length=100, default="Игрок")
    body = models.TextField()
    created = models.DateTimeField(default=timezone.now)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ('created',)

# Generated by Django 3.2.7 on 2021-10-26 13:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20211026_1138'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='statement',
            name='contact',
        ),
    ]

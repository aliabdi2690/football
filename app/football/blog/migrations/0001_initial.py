# Generated by Django 3.0a1 on 2020-05-19 12:46

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('body', models.TextField()),
                ('image', models.ImageField(upload_to='media')),
                ('summery', models.CharField(max_length=250)),
                ('slug', models.SlugField(unique=True)),
                ('pub_date', models.DateTimeField(auto_now=True)),
                ('likes', models.ManyToManyField(to=settings.AUTH_USER_MODEL, verbose_name='liked users')),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('slug', models.SlugField(unique=True)),
                ('pub_date', models.DateTimeField(auto_now=True)),
                ('post', models.ManyToManyField(to='blog.Post', verbose_name='posts related to tag')),
            ],
        ),
    ]

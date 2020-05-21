# Generated by Django 3.0a1 on 2020-05-19 12:58

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='likes',
            field=models.ManyToManyField(editable=False, to=settings.AUTH_USER_MODEL, verbose_name='liked users'),
        ),
    ]
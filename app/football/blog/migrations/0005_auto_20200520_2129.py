# Generated by Django 3.0a1 on 2020-05-20 16:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20200520_1744'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='time',
            field=models.DateTimeField(auto_now_add=True, verbose_name='comment commited'),
        ),
    ]

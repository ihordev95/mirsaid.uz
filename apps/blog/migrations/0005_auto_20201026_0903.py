# Generated by Django 3.1.2 on 2020-10-26 04:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_like'),
    ]

    operations = [
        migrations.AlterField(
            model_name='like',
            name='diz_like',
            field=models.PositiveIntegerField(null=True, verbose_name='Диз лайки'),
        ),
        migrations.AlterField(
            model_name='like',
            name='like',
            field=models.PositiveIntegerField(null=True, verbose_name='Лайки'),
        ),
    ]
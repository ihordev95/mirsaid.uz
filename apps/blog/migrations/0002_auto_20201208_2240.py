# Generated by Django 3.1.2 on 2020-12-08 17:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tag',
            options={'ordering': ['-id'], 'verbose_name': 'Tags', 'verbose_name_plural': 'Tags'},
        ),
        migrations.RemoveField(
            model_name='tag',
            name='Post',
        ),
        migrations.RemoveField(
            model_name='tag',
            name='parent',
        ),
        migrations.AddField(
            model_name='post',
            name='tag',
            field=models.ManyToManyField(to='blog.Tag', verbose_name='Tags'),
        ),
        migrations.AddField(
            model_name='tag',
            name='slug',
            field=models.SlugField(default=''),
        ),
        migrations.AlterField(
            model_name='tag',
            name='name',
            field=models.CharField(max_length=30, verbose_name='Name'),
        ),
    ]

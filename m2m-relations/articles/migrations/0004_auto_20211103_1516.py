# Generated by Django 3.2.9 on 2021-11-03 10:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0003_auto_20211103_1453'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tag',
            name='articles',
            field=models.ManyToManyField(related_name='tags', through='articles.TagToArticle', to='articles.Article'),
        ),
        migrations.AlterField(
            model_name='tagtoarticle',
            name='article',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='scopes', to='articles.article', verbose_name='Статья'),
        ),
        migrations.AlterField(
            model_name='tagtoarticle',
            name='tag',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='scopes', to='articles.tag', verbose_name='Тэг'),
        ),
    ]

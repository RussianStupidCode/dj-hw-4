# Generated by Django 3.2.9 on 2021-11-03 09:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0002_auto_20211103_1436'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tag',
            options={'ordering': ['name'], 'verbose_name': 'Тэг', 'verbose_name_plural': 'Тэги'},
        ),
        migrations.RenameField(
            model_name='tag',
            old_name='title',
            new_name='name',
        ),
        migrations.AlterField(
            model_name='tag',
            name='articles',
            field=models.ManyToManyField(related_name='scopes', through='articles.TagToArticle', to='articles.Article'),
        ),
    ]

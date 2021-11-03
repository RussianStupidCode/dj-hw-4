from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet

from .models import Article, TagToArticle, Tag


class TagToArticleInlineFormset(BaseInlineFormSet):
    def clean(self):
        # всегда должен быть 1 основной тэг -> сумма флагов == 1 (True - 1, False - 0)
        if sum([int(form.cleaned_data.get('is_main', False)) for form in self.forms]) != 1:
            raise ValidationError('Должен быть 1 основной тэг')
        return super().clean()


class TagToArticleInline(admin.TabularInline):
    model = TagToArticle
    formset = TagToArticleInlineFormset


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    inlines = [TagToArticleInline]


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    inlines = [TagToArticleInline]

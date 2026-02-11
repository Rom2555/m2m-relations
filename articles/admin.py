from django.contrib import admin

from .models import Article, Scope, Tag


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    pass


class ScopeInline(admin.TabularInline):
    model = Scope


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    inlines = [ScopeInline]

from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet

from .models import Article, Scope, Tag


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    pass

class ScopeInlineFormset(BaseInlineFormSet):
    def clean(self):
        # Подсчитываем количество основных разделов, игнорируя удалённые
        main_count = sum(
            form.cleaned_data.get('is_main', False)
            for form in self.forms
            if not form.cleaned_data.get('DELETE', False)
        )
        
        # Проверяем, что основной раздел ровно один
        if self.forms and main_count != 1:
            raise ValidationError('У статьи должен быть ровно один основной раздел')

class ScopeInline(admin.TabularInline):
    model = Scope
    formset = ScopeInlineFormset


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    inlines = [ScopeInline]



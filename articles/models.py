from django.db import models


class Article(models.Model):
    """
    Модель статьи новостного сайта.
    Имеет связь ManyToMany с Tag через промежуточную модель Scope.
    """
    title = models.CharField(max_length=256, verbose_name='Название')
    text = models.TextField(verbose_name='Текст')
    published_at = models.DateTimeField(verbose_name='Дата публикации')
    image = models.ImageField(null=True, blank=True, verbose_name='Изображение', )

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'
        ordering = ['-published_at']

    def __str__(self):
        return self.title


class Tag(models.Model):
    """
    Модель тега (раздела) для статей.
    Простое название раздела без дополнительных полей.
    """
    name = models.CharField(max_length=256, verbose_name='Название')

    class Meta:
        verbose_name = 'Раздел'
        verbose_name_plural = 'Разделы'

    def __str__(self):
        return self.name


class Scope(models.Model):
    """
    Промежуточная модель связи между Article и Tag.
    Хранит информацию о том, к каким разделам относится статья.
    Поле is_main указывает на основной раздел статьи.
    """
    # Связь с статьёй (обязательная)
    # related_name='scopes' позволяет использовать article.scopes.all() для получения Scope объектов
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='scopes')
    # Связь с тегом (разделом)
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE, related_name='scopes')
    # Флаг основного раздела - должен быть ровно один на статью
    is_main = models.BooleanField(default=False, verbose_name='Основной раздел')

    class Meta:
        # Сортировка: основной раздел первым, затем по алфавиту
        ordering = ['-is_main', 'tag__name']

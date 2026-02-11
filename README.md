# M2M Relations - Новостной сайт с тегами

Django-проект новостного сайта с реализацией связей "многие-ко-многим" через промежуточную модель Scope.

> Проект разработан в рамках учебного процесса [Нетологии](https://netology.ru/).

## Модели

### Article
Модель статьи новостного сайта.
- `title` - CharField, название статьи
- `text` - TextField, текст статьи
- `published_at` - DateTimeField, дата публикации
- `image` - ImageField, изображение статьи
- Связь ManyToMany с Tag через модель Scope

### Tag
Модель тега (раздела) для статей.
- `name` - CharField, название раздела

### Scope
Промежуточная модель связи между Article и Tag.
- `article` - ForeignKey на Article (related_name='scopes')
- `tag` - ForeignKey на Tag
- `is_main` - BooleanField, флаг основного раздела

## Особенности реализации

### Сортировка тегов
В модели Scope определена сортировка:
```python
ordering = ['-is_main', 'tag__name']
```
- основной раздел выводится первым, остальные по алфавиту.

### Валидация в админке
В `ScopeInlineFormset` реализована проверка:
- У каждой статьи должен быть ровно один основной раздел (`is_main=True`)
- При попытке сохранить без основного раздела - ошибка валидации

## Запуск проекта

0. Создайте базу данных PostgreSQL:
```bash
createdb -U postgres netology_m2m_relations
```

1. Установить зависимости:
```bash
pip install -r requirements.txt
```

2. Провести миграции:
```bash
python manage.py migrate
```

3. Загрузить тестовые данные:
```bash
python manage.py loaddata articles.json
```

4. Запустить сервер:
```bash
python manage.py runserver
```

## Админка

Доступна по адресу `/admin/`:

- создание и редактирование разделов
- редактирование статей с возможностью добавления/удаления разделов через inline-форму

## Технологии

- Django 6.0.2
- Python 3.14
- PostgreSQL (psycopg2-binary 2.9.11)
- Pillow 12.1.1

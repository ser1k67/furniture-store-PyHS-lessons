from django.contrib import admin

from catalog.models import Categories, Products

# easy way to register
# admin.site.register(Products)
# admin.site.register(Categories)


#класс для гибкой настройки отображения таблицы в админ панели
@admin.register(Categories) #регистрация таблицы в админке
class CategoriesAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}  #указывает какие поля будут заполнятся автоматический


@admin.register(Products)
class ProductsAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}

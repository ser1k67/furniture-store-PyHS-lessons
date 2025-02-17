from tabnanny import verbose
from django.apps import AppConfig


class CatalogConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'catalog'
    verbose_name = 'товары' #http://127.0.0.1:8000/admin/ 

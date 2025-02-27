from email.mime import image
from django.db import models

# https://docs.djangoproject.com/en/5.1/ref/models/fields/
# verbose - name for readers (translate or alternative version)

class Categories(models.Model):
    name = models.CharField(max_length=150, unique=True, verbose_name='название')
    slug = models.SlugField(max_length=200, unique=True, blank=True, null=True, verbose_name='URL')

    class Meta:# for names of table
        db_table = 'category'
        verbose_name = 'категория'
        verbose_name_plural = 'категории'

    def __str__(self):
        return self.name  #названия обьекта столбца https://27.0.0.1:8000/admin/catalog/categories/


class Products(models.Model):
    name = models.CharField(max_length=150, unique=True, verbose_name='название')
    slug = models.SlugField(max_length=200, unique=True, blank=True, null=True, verbose_name='URL')
    description = models.TextField(blank=True, null=True, verbose_name='описание')
    image = models.ImageField(upload_to='goods_image', blank=True, null=True, verbose_name='изображение') #upload_to= папка где будет храниться файлы
    price = models.DecimalField(default=0.00, max_digits=7, decimal_places=2, verbose_name='цена')
    discount = models.DecimalField(default=0.00, max_digits=4, decimal_places=2, verbose_name='скидка в %')
    quantity = models.PositiveIntegerField(default=0, verbose_name='количество')

    #PROTECT - не дает удалить категорию, CASCADE - удаляет все закрепленые товары, SET_DEFAULT - категория меняется на указаный дефолт
    category = models.ForeignKey(to=Categories, on_delete=models.CASCADE, verbose_name='категория') 
    


    class Meta:# for names of table
        db_table = 'product'
        verbose_name = 'товар'
        verbose_name_plural = 'товары'

    def __str__(self):
        return f"{self.name}, количество {self.quantity}"  #названия обьекта столбца https://27.0.0.1:8000/admin/catalog/categories/

    # display product id in goods from catalog pages
    def display_id(self):
        return f'{self.id:05}'
    
    
    # display price with discount in goods from catalog pages
    def display_discount_price(self):
        return round(self.price - (self.price * self.discount / 100), 2)

from django.db import models

NULLABLE = {'blank': True, 'null': True}


class Category(models.Model):
    """
    Создание модели Категория
    """
    name = models.CharField(max_length=150, verbose_name='Наименование категории')
    image = models.ImageField(upload_to='materials/', verbose_name='Изображение', **NULLABLE)
    description = models.CharField(max_length=500, verbose_name='Описание категории')
    slug = models.CharField(max_length=150, verbose_name='slug', **NULLABLE)

    def __str__(self):
        return f'{self.name}: {self.description}'

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Subcategory(models.Model):
    """
    Создание модели Подкатегория
    """
    name = models.CharField(max_length=150, verbose_name='Наименование подкатегории')
    image = models.ImageField(upload_to='materials/', verbose_name='Изображение', **NULLABLE)
    description = models.CharField(max_length=500, verbose_name='Описание подкатегории')
    slug = models.CharField(max_length=150, verbose_name='slug', **NULLABLE)

    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория pk')

    def __str__(self):
        return f'{self.name}: {self.description}'

    class Meta:
        verbose_name = 'Подкатегория'
        verbose_name_plural = 'Подкатегории'


class Product(models.Model):
    """
    Создание модели Продукт
    """

    IMAGE_CHOICES = [
        ('400*400', '400*400'),
        ('1200*536', '1200*536'),
        ('1080*1080', '1080*1080')
    ]
    name = models.CharField(max_length=150, verbose_name='Название')
    description = models.CharField(max_length=300, verbose_name='Описание')
    image = models.ImageField(upload_to='materials/', choices=IMAGE_CHOICES, verbose_name='Изображение', **NULLABLE)
    price = models.IntegerField(verbose_name='Цена')
    slug = models.CharField(max_length=150, verbose_name='slug', **NULLABLE)

    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория pk')
    subcategory = models.ForeignKey(Subcategory, on_delete=models.CASCADE, verbose_name='Подкатегория pk')

    def __str__(self):
        return f'{self.name} {self.category}'

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'





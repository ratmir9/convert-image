from django.db import models

# Create your models here.
class Product(models.Model):
    
    STATUS_CHOICES = (
        ('IN_STOCK', 'В наличии'),
        ('ON_ORDER', 'Под заказ'),
        ('EXCEPTED_TO_ARRIVE', 'Ожидается поступление'),
        ('NOT_AVAILABLE', 'Нет в наличии'),
        ('NOT_PRODUCED', 'Не производится')
    )
    
    name = models.CharField(verbose_name='Название', max_length=255, unique=True)
    type = models.CharField(verbose_name='Артикул', max_length=255)
    status = models.CharField(verbose_name='Статус', max_length=18, choices=STATUS_CHOICES)
    price = models.DecimalField(verbose_name='Цена', max_digits=8, decimal_places=2)
    image = models.ImageField(verbose_name='Изображение', upload_to='images')

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    
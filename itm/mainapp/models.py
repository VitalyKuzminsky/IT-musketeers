import datetime
import django
from django.db import models
from authapp.models import CustomUser


class Category(models.Model):
    """Описание модели Категория услуги"""
    name = models.CharField(max_length=128, verbose_name='Наименование')
    description = models.TextField(verbose_name='Описание')
    images = models.FileField(blank=True, null=True, upload_to='category/', verbose_name='Фото')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Категория услуги'
        verbose_name_plural = 'Категории услуги'


class Services(models.Model):
    """Описание модели Услуги"""
    name = models.CharField(max_length=128, verbose_name='Наименование')
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория')
    custom_user_id = models.ForeignKey(CustomUser, on_delete=models.CASCADE, verbose_name='Автор работы')
    development_time = models.IntegerField(
        help_text='Введите ориентировочный срок разработки',
        verbose_name='Время разработки в днях'
    )
    description = models.TextField(blank=True, null=True, verbose_name='Описание')
    price = models.DecimalField(max_digits=8, decimal_places=2, verbose_name='Стоимость услуги')
    photo = models.FileField(blank=True, null=True, upload_to='services/', verbose_name='Фото')
    deleted = models.BooleanField(default=False, verbose_name='Удалено')  # помечаем удалённым

    def __str__(self):
        return f'{self.name} {self.custom_user_id}'

    class Meta:
        verbose_name = 'Услуга'
        verbose_name_plural = 'Услуги'

    def delete(self, *args, **kwargs):
        """Переопределяем метод, т.к. мы не удаляем совсем, а только помечаем, как удалённое"""
        self.deleted = True
        self.save()


class Reviews(models.Model):
    """Описание модели Отзывы"""
    custom_user_id = models.ForeignKey(CustomUser, on_delete=models.CASCADE, verbose_name='Автор')
    services_id = models.ForeignKey(Services, on_delete=models.CASCADE, verbose_name='Услуга')
    content = models.TextField(verbose_name='Текст')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Создан')
    updated_at = models.DateTimeField(blank=True, null=True, verbose_name='Обновлен')
    estimation = models.CharField(blank=True, null=True, max_length=5, verbose_name='Оценка')
    deleted = models.BooleanField(default=False, verbose_name='Удален')  # помечаем удалённым

    def __str__(self):
        return f'{self.custom_user_id} {self.services_id}'

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'

    def delete(self, *args, **kwargs):
        """Переопределяем метод, т.к. мы не удаляем совсем, а только помечаем, как удалённое"""
        self.deleted = True
        self.save()


class Basket(models.Model):
    """Описание модели Корзина"""
    custom_user_id = models.ForeignKey(CustomUser, on_delete=models.CASCADE, verbose_name='Клиент')
    service_id = models.ForeignKey(Services, on_delete=models.CASCADE, verbose_name='Услуга')
    create_date = models.DateTimeField(auto_now_add=True, verbose_name='Время заявки')
    pay_date = models.DateTimeField(null=True, blank=True, verbose_name='Время оплаты')

    def __str__(self):
        return f'{self.custom_user_id} {self.service_id} {self.price} {self.status}'

    class Meta:
        verbose_name = 'Корзина'


class WorkExample(models.Model):
    """Описание модели Фотографии_примеров_наших_работ"""
    services_id = models.ForeignKey(Services, on_delete=models.CASCADE, verbose_name='Услуга')
    photo = models.FileField(blank=True, null=True, upload_to='library/', verbose_name='Фото')
    deleted = models.BooleanField(default=False, verbose_name='Удален')  # помечаем удалённым

    def __str__(self):
        return f'{self.photo}'

    class Meta:
        verbose_name = 'Фото нашей работы'
        verbose_name_plural = 'Фотографии наших работ'

    def delete(self, *args, **kwargs):
        """Переопределяем метод, т.к. мы не удаляем совсем, а только помечаем, как удалённое"""
        self.deleted = True
        self.save()

from django.db import models
from authapp.models import CustomUser


class Category(models.Model):
    """Описание модели Категория услуги"""
    name = models.CharField(max_length=128, verbose_name='Наименование')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Категория услуги'
        verbose_name_plural = 'Категории услуги'


class Services(models.Model):
    """Описание модели Услуги"""
    name = models.CharField(max_length=128, verbose_name='Наименование')
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория')
    custom_user_id = models.ForeignKey(CustomUser, on_delete=models.CASCADE, verbose_name='Клиент')
    development_time = models.DateField(help_text='Введите ориентировочный срок разработки',
                                       verbose_name='Время разработки в днях')
    price = models.DecimalField(max_digits=8, decimal_places=2, verbose_name='Стоимость услуги')
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
    updated_at = models.DateTimeField(auto_now_add=True, verbose_name='Обновлен')
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
    BASKET_STATUS = [
        ('PAYED', 'Оплачено'),
        ('UNPAYED', 'Не оплачено')
    ]

    custom_user_id = models.ForeignKey(CustomUser, on_delete=models.CASCADE, verbose_name='Клиент')
    service_id = models.ForeignKey(Services, on_delete=models.CASCADE, verbose_name='Услуга')
    price = models.PositiveIntegerField(verbose_name='Стоимость услуги')
    status = models.CharField(max_length=50, choices=BASKET_STATUS, default=BASKET_STATUS[1][0],
                              verbose_name='Статус оплаты заказа')

    def __str__(self):
        return f'{self.custom_user_id} {self.service_id} {self.price} {self.status}'

    class Meta:
        verbose_name = 'Корзина'

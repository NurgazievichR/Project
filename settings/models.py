from turtle import mode
from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField

class Network(models.Model):
    NETWORKS = [
        ('facebook','facebook'),
        ('twitter','twitter'),
        ('instagram','instagram'),
        ('youtube','youtube'),
        ('soundcloud','soundcloud'),
        ('internet','internet'),
    ]
    network = models.CharField('Сеть', max_length=100, choices=NETWORKS, unique=True)
    address = models.CharField('Ссылка', max_length=255, help_text='Введите ссылку на вашу социальную сеть')
    amount = models.IntegerField('Количество подписчиков', help_text='Укажите количество подписчиков')

    def __str__(self):
        return self.network

    class Meta:
        verbose_name = 'Соцсеть'
        verbose_name_plural = 'Соцсети'

class Advertisement(models.Model):
    TYPES = [
        ('370x442','370x442'),
        ('846x155','846x155'),
    ]
    type = models.CharField('Тип', max_length=100, choices=TYPES, unique=True)
    address = models.CharField('Ссылка', max_length=255, help_text='Введите ссылку на рекламу')
    image = models.ImageField('Фото', upload_to='advertisement/',help_text='фотография должна быть того размера, как вы указали' )

    def __str__(self):
        return self.type

    class Meta:
        verbose_name = 'Реклама'
        verbose_name_plural = 'Рекламы'

class About(models.Model):
    TYPE = [('about', 'about'),]
    type = models.CharField(max_length=100, choices=TYPE, default='about', unique=True)
    name = models.CharField('Имя', max_length=255)
    image = models.ImageField('Фото', upload_to='about/')
    description = models.TextField('Описание')
    email = models.EmailField('Email')

    def __str__(self):
        return self.type

    class Meta:
        verbose_name = 'О вас'
        verbose_name_plural = 'О вас'
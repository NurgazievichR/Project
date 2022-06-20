# Generated by Django 4.0.5 on 2022-06-18 14:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Advertisement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('370x442', '370x442'), ('846x155', '846x155')], max_length=100, unique=True, verbose_name='Тип')),
                ('address', models.SlugField(help_text='Введите ссылку на рекламу', max_length=255, verbose_name='Ссылка')),
                ('image', models.ImageField(help_text='фотография должна быть того размера, как вы указали', upload_to='advertisement/', verbose_name='Фото')),
            ],
            options={
                'verbose_name': 'Реклама',
                'verbose_name_plural': 'Рекламы',
            },
        ),
        migrations.CreateModel(
            name='Network',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('network', models.CharField(choices=[('facebook', 'facebook'), ('twitter', 'twitter'), ('instagram', 'instagram'), ('youtube', 'youtube'), ('soundcloud', 'soundcloud'), ('internet', 'internet')], max_length=100, unique=True, verbose_name='Сеть')),
                ('address', models.SlugField(help_text='Введите ссылку на вашу социальную сеть', max_length=255, verbose_name='Ссылка')),
                ('amount', models.IntegerField(help_text='Укажите количество подписчиков', verbose_name='Количество подписчиков')),
            ],
            options={
                'verbose_name': 'Соцсеть',
                'verbose_name_plural': 'Соцсети',
            },
        ),
    ]
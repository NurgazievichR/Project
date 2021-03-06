# Generated by Django 4.0.5 on 2022-06-16 13:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dishes', '0002_alter_category_icon_alter_category_icon2'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ['-id'], 'verbose_name': 'Категория', 'verbose_name_plural': 'Категории'},
        ),
        migrations.AddField(
            model_name='category',
            name='image',
            field=models.ImageField(blank=True, upload_to='category_images/', verbose_name='Фото'),
        ),
    ]

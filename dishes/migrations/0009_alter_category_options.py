# Generated by Django 4.0.5 on 2022-06-18 14:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dishes', '0008_alter_product_cuisine'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'Категория', 'verbose_name_plural': 'Категории'},
        ),
    ]

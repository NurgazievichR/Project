# Generated by Django 4.0.5 on 2022-06-17 10:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dishes', '0007_alter_tag_options_product_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='cuisine',
            field=models.CharField(choices=[('Italian', 'Italian'), ('Japanese', 'Japanese'), ('Thai', 'Thai'), ('Russian', 'Russian'), ('Korean', 'Korean'), ('Chinese', 'Chinese'), ('American', 'American')], max_length=100, verbose_name='Страна'),
        ),
    ]

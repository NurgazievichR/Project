# Generated by Django 4.0.5 on 2022-06-20 05:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('settings', '0004_about'),
    ]

    operations = [
        migrations.AlterField(
            model_name='about',
            name='description',
            field=models.TextField(verbose_name='Описание'),
        ),
    ]
# Generated by Django 4.2.6 on 2023-12-10 19:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bboard', '0002_remove_apartment_furniture_remove_apartment_repair_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apartment',
            name='parking',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Парковка'),
        ),
    ]
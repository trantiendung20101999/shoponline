# Generated by Django 3.2.4 on 2021-06-18 09:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_alter_product_date_release'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='date_release',
            field=models.DateTimeField(default=''),
        ),
    ]
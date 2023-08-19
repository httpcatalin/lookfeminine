# Generated by Django 4.2.4 on 2023-08-19 22:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0007_remove_product_size_alter_product_colors'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='size_category',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='products_with_size_category', to='base.category'),
        ),
    ]

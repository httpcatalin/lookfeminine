# Generated by Django 4.2.3 on 2023-07-24 15:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_rename_size_product_size'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='colors',
            field=models.ManyToManyField(null=True, to='base.color'),
        ),
    ]
# Generated by Django 4.0.3 on 2022-07-10 04:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_rename_product_description_product_product_description'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='category',
        ),
        migrations.RemoveField(
            model_name='productimage',
            name='product',
        ),
        migrations.DeleteModel(
            name='Category',
        ),
        migrations.DeleteModel(
            name='Product',
        ),
        migrations.DeleteModel(
            name='ProductImage',
        ),
    ]

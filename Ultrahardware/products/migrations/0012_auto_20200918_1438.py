# Generated by Django 3.0.2 on 2020-09-18 17:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0011_auto_20200918_1429'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='product_id',
            new_name='category_id',
        ),
        migrations.RenameField(
            model_name='category_parent',
            old_name='product_id',
            new_name='categoryParent_id',
        ),
    ]

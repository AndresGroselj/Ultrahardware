# Generated by Django 3.0.2 on 2020-09-17 20:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0008_auto_20200917_1648'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='imagen_principal',
            field=models.ImageField(blank=True, default='productDefault.png', null=True, upload_to=''),
        ),
    ]

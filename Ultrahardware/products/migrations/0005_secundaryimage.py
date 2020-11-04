# Generated by Django 3.0.2 on 2020-11-04 13:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_delete_secundaryimage'),
    ]

    operations = [
        migrations.CreateModel(
            name='SecundaryImage',
            fields=[
                ('SecundaryImage_id', models.AutoField(primary_key=True, serialize=False)),
                ('imagen_principal', models.ImageField(blank=True, default='productDefault.png', null=True, upload_to='')),
                ('active', models.BooleanField()),
                ('order', models.IntegerField(default=0)),
                ('product_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='products.Product')),
            ],
        ),
    ]

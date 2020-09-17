from django.db import models


# Create your models here.

class Product(models.Model):
    product_id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50, blank=True, null=True)
    imagen_principal = models.ImageField(blank=True, null=True, default="productDefault.png")
    precio = models.IntegerField()
    stock = models.IntegerField()
    description = models.TextField(blank=True, null=True)
    specs = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nombre

    def toJson(self):
        pass


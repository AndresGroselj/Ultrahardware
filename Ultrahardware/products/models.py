from django.db import models
import json

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
        val = {str(self.product_id): {
            'nombre': self.nombre,
            'imagen_principal': self.imagen_principal.url,
            'precio': self.precio,
            'stock': self.stock,
            'description': self.description,
            }}
        
        return json.dumps(val)


def productsToJson(products):
    producLib = {}
    for product in products:
        lib = {str(product.product_id): {
            'nombre': product.nombre,
            'imagen_principal': product.imagen_principal.url,
            'precio': product.precio,
            'stock': product.stock,
            # 'description': product.description,
            }}
        producLib = {**producLib, **lib}
    return json.dumps(producLib)
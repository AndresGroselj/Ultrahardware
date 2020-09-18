from django.db import models
import json

# Create your models here.

class Category_parent(models.Model):
    categoryParent_id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50, blank=True, null=True)
    order = models.IntegerField(default=0)

    def __str__(self):
        return self.nombre

    @property
    def Categorias(self):
        return Category.objects.filter(parent_id=self.categoryParent_id).order_by("order")

class Category(models.Model):
    category_id = models.AutoField(primary_key=True)
    parent_id = models.ForeignKey(Category_parent, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=50, blank=True, null=True)
    order = models.IntegerField(default=0)

    def __str__(self):
        return self.nombre

class Product(models.Model):
    product_id = models.AutoField(primary_key=True)
    category_id = models.ForeignKey(Category_parent, null=True, on_delete=models.SET_NULL)
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
    
    # @property
    # def test(self):
    #     return  [1,2,3]
    # {% for n in product.test %}<h1>{{n}}</1>{% endfor %}

    # @property
    # def test(h):
    #     return "testSuccess"
    #<h1>{{ product.test }}</h1>


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
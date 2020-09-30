from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from datetime import date
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
    category_id = models.ForeignKey(Category, null=True, on_delete=models.SET_NULL)
    nombre = models.CharField(max_length=50, blank=True, null=True)
    imagen_principal = models.ImageField(blank=True, null=True, default="productDefault.png")
    precio = models.IntegerField()
    stock = models.IntegerField()
    description = models.TextField(blank=True, null=True)
    specs = models.TextField(blank=True, null=True)
    views = models.IntegerField(default=0)

    def __str__(self):
        return self.nombre
    
    @property
    def formatedPrice(self):
        return "${:,.0f}".format(self.precio)
    
    @property
    def FullPrice(self):
        descuentos = Discount.objects.filter(product_id=self.product_id)
        isDiscounted = False
        discount = 0
        discountFloat = 0
        for d in descuentos:
            if d.startDate <= date.today() <= d.endDate:
                isDiscounted = True
                discount = d.discount
                discountFloat = d.DiscountToFloat
                break
        originalPrice = "${:,.0f}".format(self.precio)
        totalPrice = "${:,.0f}".format(round(self.precio * (1 - discountFloat)))
        return (isDiscounted, discount, originalPrice, totalPrice)

class Discount(models.Model):
    Discount_id = models.AutoField(primary_key=True)
    product_id = models.ForeignKey(Product, null=True, on_delete=models.SET_NULL)
    discount = models.IntegerField(default=10,
    validators=[
            MaxValueValidator(100),
            MinValueValidator(1)
        ])
    startDate = models.DateField()
    endDate = models.DateField()

    def __str__(self):
        return f"{self.Discount_id}: {self.product_id.nombre} | {self.discount}%"
    
    @property
    def DiscountToFloat(self):
        return self.discount / 100
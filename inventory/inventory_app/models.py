from django.db import models

# Brands
class Brand(models.Model):
    class Meta:
        verbose_prural_name = 'Brands'

    name = models.CharField(max_length=100)
    description = models.CharField(max_length=200)

    def __str__(self):
        return self.name
    
# Category
class Category(models.Model):
    class Meta:
        verbose_prural_name = 'Categories'

    name = models.CharField(max_length=100)
    description = models.CharField(max_length=200)

    def __str__(self):
        return self.name
    
# Warehouse
class Warehouse(models.Model):
    class Meta:
        verbose_prural_name = 'Warehouses'

    name = models.CharField(max_length=100)    
    description = models.CharField(max_length=200)

    def __str__(self):    
        return self.name
    
# Product
class Product(models.Model):
    code = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.code} - {self.description}"
    
# InventoryProduct
class InventoryProduct(models.Model):
    class Meta:
        verbose_prural_name = 'InventoryProducts'

    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    warehouse = models.ForeignKey(Warehouse, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0) 
    
    def __str__(self):
        return f"{self.quantity} - {self.product}  ({self.warehouse})"  
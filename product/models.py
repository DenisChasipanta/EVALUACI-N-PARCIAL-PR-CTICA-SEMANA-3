from django.db import models

# Create your models here.
class Product (models.Model):
    title= models.CharField(max_length=100,verbose_name="Titulo")
    description= models.TextField(verbose_name="Descripcion")
    image= models.ImageField(upload_to="product",verbose_name="Imangen")
    created= models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated= models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

    class Meta:
        verbose_name="product"
        verbose_name_plural="products"
        ordering=["-created"]

    def __str__(self):
        return  self.title

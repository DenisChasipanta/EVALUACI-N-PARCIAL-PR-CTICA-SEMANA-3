from django.contrib import admin
from .models import Product
class ProyectAdmin(admin.ModelAdmin):
    readonly_fields=("created", "updated")
# Register your models here.
admin.site.register(Product, ProyectAdmin)
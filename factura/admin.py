# Register your models here.
from django.contrib import admin
from factura.models import Articulo, Factura


class AdminFactura(admin.ModelAdmin):
    date_hierarchy = "fecha_emision"
    list_display = ["pk", "num", "fecha_emision", "cliente_nombre"]


admin.site.register(Factura, AdminFactura)


class AdminArticulo(admin.ModelAdmin):
    list_display = [
        "pk",
        "nombre_producto",
        "precio_unitario",
        "unidades",
    ]


admin.site.register(Articulo, AdminArticulo)
# Register your models here.

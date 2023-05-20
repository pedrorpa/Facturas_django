from django.db import models

# Create your models here.


class Factura(models.Model):
    class Meta:
        verbose_name = "Facturas"
        verbose_name_plural = "Facturas"

    id = models.AutoField(primary_key=True)

    num = models.CharField(
        verbose_name="Numero Factura",
        max_length=12,
        unique=True,
    )

    anio = models.DateTimeField(
        auto_now_add=True,
    )

    fecha_emision = models.DateTimeField(
        auto_now_add=True,
    )

    cliente_nombre = models.CharField(
        verbose_name="Nombre del cliente",
        max_length=18,
    )

    cliente_direccion = models.CharField(
        verbose_name="Direccion cliente",
        max_length=120,
    )

    def __str__(self):
        return self.num


class Articulo(models.Model):
    class Meta:
        verbose_name = "Linea factura"
        verbose_name_plural = "Lineas Facturas"

    id = models.AutoField(primary_key=True)

    nombre_producto = models.CharField(
        verbose_name="Nombre de producto",
        max_length=24,
    )
    precio_unitario = models.IntegerField(
        verbose_name="Precio unitario",
    )
    unidades = models.IntegerField(
        verbose_name="Unidades",
    )
    factura = models.ForeignKey(
        Factura,
        verbose_name="Factura",
        on_delete=models.PROTECT,
        related_name="lineafactura",
    )

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    """
    def __str__(self):
        return self.name
    """

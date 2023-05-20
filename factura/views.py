from django.shortcuts import redirect, render
from factura.models import Articulo, Factura

# Create your views here.


# Create your views here.
def homepage(request):
    facturas = Factura.objects.all()
    return render(
        request,
        "factura/homepage.html",
        {
            "title": "Gestion de Facturas",
            "facturas": facturas,
        },
    )


def lista_factura(request, pk):
    facturas = Factura.objects.filter(pk=pk)
    return render(
        request,
        "factura/list_factura.html",
        {
            "title": "Facturas",
            "facturas": facturas,
        },
    )


def detalle_factura(request, factura_id):
    factura = Factura.objects.get(pk=factura_id)
    articulos = Articulo.objects.filter(factura=factura)

    total = 0
    for articulo in articulos:
        precio_total = articulo.precio_unitario * articulo.unidades
        total += precio_total

    return render(
        request,
        "factura/detalle_factura.html",
        {
            "factura": factura,
            "articulos": articulos,
            "total": total,
        },
    )

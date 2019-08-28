from django.shortcuts import render
from .models import Productos

# Create your views here.
def producto_list(request):
    product = Productos.objects.all()
    return render(request, 'producto/producto.html', {'productos1':product})
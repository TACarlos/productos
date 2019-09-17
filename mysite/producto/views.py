from django.shortcuts import render, HttpResponseRedirect, get_object_or_404
from .models import Productos
from .forms import ProdForm

# Create your views here.
def producto_list(request):
    product = Productos.objects.all()
    return render(request, 'producto/producto.html', {'productos1':product})

def lista_prod(request):
    lista = Productos.objects.all
    if request.method == "POST":
        form = ProdForm(request.POST)
        if form.is_valid():
            prod = form.save(commit=False)
            prod.save()
            return HttpResponseRedirect('/productos')
        else:
            print("error de validacion")
            
    else:
        form = ProdForm() 
        print("no es un post")   
    return render(request, 'producto/lista_prod.html', {'productos':lista,'form':form})

def detalle_prod(request, pk):
    prod = get_object_or_404(Productos, pk=pk)
    return render(request, 'producto/detalle_prod.html', {'prod': prod})
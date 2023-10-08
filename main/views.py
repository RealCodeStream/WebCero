from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.decorators import login_required
from .forms import CategoriaForm

#@login_required
def index(request):
    return render(request, 'main/index.html')


def review(request):
    return render(request, 'main/review.html')

def categorias(request):
    return render(request, 'main/Categorias.html')

def Gestion(request):
    return render(request, 'main/Gestion.html')
# Create your views here.

def crear_categoria(request):
    if request.method == 'POST':
        form = CategoriaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('main:Categoria')  # Redirige a la página de categorías después de crear una nueva categoría
    else:
        form = CategoriaForm()
    
    # Obtén la lista de categorías existentes
    categorias = Categoria.objects.all()

    return render(request, 'main/Categorias.html', {'form': form, 'categorias': categorias})


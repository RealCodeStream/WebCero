from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

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

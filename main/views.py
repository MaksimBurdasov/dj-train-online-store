from django.shortcuts import render, redirect
from django.http import HttpResponse

from .forms import ProductForm
from .models import Product


# # Create your views here.
# def template(request):
#     return HttpResponse("<h1>Template of use HttpResponse</h1>")


def index(request):
    products = Product.objects.all().order_by('id')
    return render(request, 'main/index.html', {'title': 'Главная', 'products': products})


def add_product(request):
    error = ''
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'Ошибка при заполнении формы!'

    form = ProductForm()
    context = {
        'title': 'Добавить новый товар',
        'error': error,
        'form': form
    }
    return render(request, 'main/add_product.html', context)


def about(request):
    return render(request, 'main/about.html', {'title': 'О нас'})
from django.shortcuts import render, get_object_or_404, redirect
from .models import Product
from .forms import ProductForm

def product_list(request):
    products = Product.objects.all()
    return render(request, "products/product_list.html", {"products": products})

def product_detail(request, id):
    product = get_object_or_404(Product, id=id)
    return render(request, "products/product_detail.html", {"product": product})

def product_create(request):
    if request.method == "POST":
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("product_list")
    else:
        form = ProductForm()
        
    return render(request, "products/product_form.html", {"form": form})

def product_update(request, id):
    product = get_object_or_404(Product, id=id)
    if request.method == "POST":
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect("product_list")
    else:
        form = ProductForm(instance=product)
        
    return render(request, "products/product_form.html", {"form": form})

def product_delete(request, id):
    product = get_object_or_404(Product, id=id)
    product.delete()
    return redirect("product_list")
from django.shortcuts import render
from .models import Product, SizeVarient, ColorVarient


# Create your views here.
def index(request):
    return render(request, "product/product.html", {"products": Product.objects.all()})


def product_detail_page(request, slug):
    product_obj = Product.objects.get(product_slug=slug)
    size_product_value = 0
    color_product_value = 0
    if request.GET.get('size'):
        size_name = request.GET.get('size')
        size_obj = SizeVarient.objects.get(size_name=size_name)
        size_product_value = size_obj.product_value

    if request.GET.get('color'):
        color_name = request.GET.get('color')
        color_obj = ColorVarient.objects.get(color_name=color_name)
        color_product_value = color_obj.product_value

    return render(request, "product/product_details.html", {
        "product_obj": product_obj,
        "products": Product.objects.all(),
        "product_value": product_obj.product_value + size_product_value + color_product_value,
        "selected_size": request.GET.get('size'),
        "selected_color": request.GET.get('color'),
    }
    )

from django.shortcuts import render
from .models import Product


# Create your views here.
def index(request):
    return render(request, "product/product.html", {"products": Product.objects.all()})


def product_detail_page(request, slug):
    product_obj = Product.objects.get(product_slug=slug)
    return render(request, "product/product_details.html", {
        "product_obj": product_obj,
        "products": Product.objects.all()
    }
    )

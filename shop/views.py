from django.shortcuts import render, get_object_or_404
from cart.forms import CartAddProductForm
from .models import Category, Product


def product_list(request, category_slug=None):
    # #print(f"\n\nRequest Method------> {request.method}")
    # #print(f"GET query parameters: {request.GET.dict()}")
    category = None
    categories = Category.objects.all()
    # #print(f"categories:  {categories}")
    products = Product.objects.filter(available=True)
    # #print(f"products:  {products}")
    # #print(f"category_slug: {category_slug}")
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    return render(request,
                  'shop/product/list.html',
                  {'category': category,
                   'categories': categories,
                   'products': products})


def product_detail(request, id, slug):
    #print("inside product details.","\n\n\n")
    product = get_object_or_404(Product,
                                id=id,
                                slug=slug,
                                available=True)
    cart_product_form = CartAddProductForm()
    #print("inside product details. 2","\n\n\n")
    return render(request,
                  'shop/product/detail.html',
                  {'product': product,
                   'cart_product_form': cart_product_form})

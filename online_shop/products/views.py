from django.shortcuts import render, get_object_or_404, redirect
from .models import Product, Category, Favorite, CartItem, Review
from django.contrib.auth.decorators import login_required
from django.template.defaultfilters import floatformat


def product_list(request, category_slug=None):
    categories = Category.objects.all()
    products = Product.objects.all()
    selected_category = None
    
    if category_slug:
        selected_category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=selected_category)

    return render(request, 'products/product_list.html', {
        'categories': categories,
        'products': products,
        'selected_category': selected_category,
    })


def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    reviews = Review.objects.filter(product=product)
    return render(request, 'products/product_detail.html', {'product': product, 'reviews': reviews})

def category_list(request):
    categories = Category.objects.all()
    return render(request, 'products/category_list.html', {'categories': categories})

def product_by_category(request, slug):
    category = get_object_or_404(Category, slug=slug)
    products = category.products.all()
    return render(request, 'products/product_by_category.html', {
        'category': category,
        'products': products
    })

@login_required
def increase_cart_quantity(request, product_id):
    if request.method == 'POST':
        product = get_object_or_404(Product, id=product_id)
        cart_item, created = CartItem.objects.get_or_create(user=request.user, product=product)

        cart_item.quantity += 1
        cart_item.save()

    return redirect('view_cart')


@login_required
def decrease_cart_quantity(request, product_id):
    if request.method == 'POST':
        try:
            cart_item = CartItem.objects.get(user=request.user, product_id=product_id)
            cart_item.quantity -= 1
            if cart_item.quantity <= 0:
                cart_item.delete()
            else:
                cart_item.save()
        except CartItem.DoesNotExist:
            pass

    return redirect('view_cart')


@login_required
def add_to_favorites(request, pk):
    product = get_object_or_404(Product, pk=pk)
    Favorite.objects.get_or_create(user=request.user, product=product)
    return redirect('product_list')

@login_required
def add_to_cart(request, pk):
    product = get_object_or_404(Product, pk=pk)
    item, created = CartItem.objects.get_or_create(user=request.user, product=product)
    if not created:
        item.quantity += 1
        item.save()
    return redirect('product_detail', pk=pk)

@login_required
def submit_review(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        content = request.POST.get('content')
        rating = request.POST.get('rating')
        Review.objects.create(user=request.user, product=product, content=content, rating=rating)
    return redirect('product_detail', pk=pk)

@login_required
def view_cart(request):
    items = CartItem.objects.filter(user=request.user)
    return render(request, 'products/view_cart.html', {'items': items})

@login_required
def view_favorites(request):
    items = Favorite.objects.filter(user=request.user)
    return render(request, 'products/view_favorites.html', {'items': items})

@login_required
def remove_from_favorites(request, pk):
    item = get_object_or_404(Favorite, pk=pk, user=request.user)
    item.delete()
    return redirect('view_favorites')


@login_required
def view_cart(request):
    items = CartItem.objects.filter(user=request.user)
    total_price = sum(item.product.price * item.quantity for item in items)

    return render(request, 'products/view_cart.html', {
        'items': items,
        'total_price': total_price
    })

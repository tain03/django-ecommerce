from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Cart
from book.models import Book

@login_required
def add_to_cart(request, book_id):
    book = Book.objects.get(id=book_id)
    cart_item, created = Cart.objects.get_or_create(
        customer=request.user,
        book=book
    )
    if not created:
        cart_item.quantity += 1
        cart_item.save()
    return redirect('cart:view_cart')

@login_required
def view_cart(request):
    cart_items = Cart.objects.filter(customer=request.user)
    cart_total = sum(item.get_total() for item in cart_items)
    return render(request, 'cart/cart.html', {
        'cart_items': cart_items,
        'cart_total': cart_total
    })

@login_required
def update_quantity(request, cart_item_id):
    if request.method == 'POST':
        cart_item = get_object_or_404(Cart, id=cart_item_id, customer=request.user)
        quantity = int(request.POST.get('quantity', 1))
        if quantity > 0:
            cart_item.quantity = quantity
            cart_item.save()
    return redirect('cart:view_cart')

@login_required
def remove_from_cart(request, cart_item_id):
    cart_item = get_object_or_404(Cart, id=cart_item_id, customer=request.user)
    cart_item.delete()
    return redirect('cart:view_cart')
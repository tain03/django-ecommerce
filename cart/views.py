from django.shortcuts import render, redirect
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
    return render(request, 'cart/cart.html', {'cart_items': cart_items})
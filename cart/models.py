from django.db import models
from customer.models import Customer
from book.models import Book

class Cart(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.customer.username}'s cart - {self.book.title}"
    
    def get_total(self):
        return self.quantity * self.book.price
    
    def cart_total(self):
        cart_items = Cart.objects.filter(customer=self.customer)
        total = 0
        for item in cart_items:
            total += item.get_total()
        return total
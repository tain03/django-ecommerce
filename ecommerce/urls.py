from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('book.urls')),
    path('customer/', include('customer.urls')),
    path('cart/', include('cart.urls')),
]
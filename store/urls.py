from django.urls import path
from .views import (
    store,
    cart,
    checkout,
    update_item,
    get_cart_total
)


urlpatterns =  [
    path('', store, name='store'),
    path('cart/', cart, name='cart'),
    path('checkout/', checkout, name='checkout'),
    path('update_item/', update_item, name='update_item'),
    path('get_cart_total/', get_cart_total, name='get_cart_total'),
]
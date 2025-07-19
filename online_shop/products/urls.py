from django.urls import path
from .views import (
    product_list,
    product_detail,
    add_to_favorites,
    add_to_cart,
    submit_review,
    view_cart,
    view_favorites,
    remove_from_favorites,
    increase_cart_quantity,
    decrease_cart_quantity,
)

urlpatterns = [
    path('', product_list, name='product_list'),
    path('category/<slug:category_slug>/', product_list, name='products_by_category'),
    path('product/<int:pk>/', product_detail, name='product_detail'),
    path('product/<int:pk>/favorite/', add_to_favorites, name='add_to_favorites'),
    path('product/<int:pk>/cart/', add_to_cart, name='add_to_cart'),
    path('product/<int:pk>/review/', submit_review, name='submit_review'),

    # Корзина и избранное
    path('cart/', view_cart, name='view_cart'),
    path('cart/increase/<int:product_id>/', increase_cart_quantity, name='increase_cart_quantity'),
    path('cart/decrease/<int:product_id>/', decrease_cart_quantity, name='decrease_cart_quantity'),
    path('favorites/', view_favorites, name='view_favorites'),
    path('favorites/remove/<int:pk>/', remove_from_favorites, name='remove_from_favorites'),
]

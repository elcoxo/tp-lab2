from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('cart', views.cart, name='cart'),
    path("add_to_cart", views.add_to_cart, name= "add"),
    path("delete_item", views.delete_item, name= "delete"),
    path('buy/<int:product_id>/', views.PurchaseCreate.as_view(), name='buy'),
]

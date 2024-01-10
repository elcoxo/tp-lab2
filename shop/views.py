from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.edit import CreateView
from django.http import JsonResponse
import json
from .models import Product, Purchase, Cart, CartItem

# Create your views here.
def index(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'shop/index.html', context)

def cart(request):
    cart = None
    cartitems = []
    
    cart, created = Cart.objects.get_or_create(completed=False)
    cartitems = cart.cartitems.all()
    
    context = {"cart":cart, "products":cartitems}
    return render(request, "shop/cart.html", context)

def add_to_cart(request):
    data = json.loads(request.body)
    product_id = data["id"]
    product = Product.objects.get(id=product_id)
    
    cart, created = Cart.objects.get_or_create(completed=False)
    cartitem, created =CartItem.objects.get_or_create(cart=cart, product=product)
    cartitem.quantity += 1
    cartitem.save()
    
    
    num_of_item = cart.num_of_items
    
    print(cartitem)
    return JsonResponse(num_of_item, safe=False)

def delete_item(request):
    data = json.loads(request.body)
    product_id = data["id"]
    product = Product.objects.get(id=product_id)
    cart, created = Cart.objects.get_or_create(completed=False)
    cartitem, created =CartItem.objects.get_or_create(cart=cart, product=product)
    cartitem.delete()

    num_of_item = cart.num_of_items

    print(num_of_item)
    return JsonResponse(num_of_item, safe=False)

class PurchaseCreate(CreateView):
    model = Purchase
    fields = ['product', 'person', 'address']

    def form_valid(self, form):
        self.object = form.save()
        return HttpResponse(f'Спасибо за покупку, {self.object.person}!')


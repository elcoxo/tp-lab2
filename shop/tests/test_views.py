from django.test import TestCase, Client
from shop.views import PurchaseCreate
from shop.models import Product, Purchase, Cart, CartItem
from django.urls import reverse


class PurchaseCreateTestCase(TestCase):
    def setUp(self):
        self.client = Client()

    def test_webpage_accessibility(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

class CartTests(TestCase):
    def setUp(self) -> None:
        self.product = Product.objects.create(name="Guinness", price="200")

    def test_add_to_cart(self):
        response = self.client.post(reverse('add'), {'id': self.product.id}, content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(Cart.objects.count(), 1)
        self.assertEqual(CartItem.objects.count(), 1)
        self.assertEqual(Cart.objects.first().num_of_items, 1)

    def test_remove_from_cart(self):
        response = self.client.post(reverse('add'), {'id': self.product.id}, content_type='application/json')
        self.assertEqual(response.status_code, 200)

        response = self.client.post(reverse('delete'), {'id': self.product.id}, content_type='application/json')
        self.assertEqual(response.status_code, 200)
        cart = Cart.objects.get(completed=False)
        cart_items = CartItem.objects.filter(cart=cart)
        self.assertEqual(len(cart_items), 0)

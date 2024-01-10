from django.test import TestCase
from shop.models import Product, Purchase, Cart, CartItem
from datetime import datetime
from django.urls import reverse

class ProductTestCase(TestCase):
    def setUp(self):
        Product.objects.create(name="Guinness", price="200")
        Product.objects.create(name="pencil", price="50")

    def test_correctness_types(self):                   
        self.assertIsInstance(Product.objects.get(name="Guinness").name, str)
        self.assertIsInstance(Product.objects.get(name="Guinness").price, int)
        self.assertIsInstance(Product.objects.get(name="pencil").name, str)
        self.assertIsInstance(Product.objects.get(name="pencil").price, int)        

    def test_correctness_data(self):
        self.assertTrue(Product.objects.get(name="Guinness").price == 200)
        self.assertTrue(Product.objects.get(name="pencil").price == 50)

class ProductOrder(TestCase):
    def setUp(self) -> None:
        self.product = Product.objects.create(name="Guinness", price="200")

    def test_order_total(self):
        # Добавляем несколько товаров в корзину
        response = self.client.post(reverse('add'), {'id': self.product.id}, content_type='application/json')
        self.assertEqual(response.status_code, 200)

        #another_product = Product.objects.create(name='Guinness', price=200)
        response = self.client.post(reverse('add'), {'id': self.product.id}, content_type='application/json')
        self.assertEqual(response.status_code, 200)

        # Проверяем, что сумма заказа рассчитана верно
        response = self.client.get(reverse('cart'))
        self.assertEqual(response.status_code, 200)

        cart, created = Cart.objects.get_or_create(completed=False)
        self.assertEqual(cart.num_of_items, 2)

        cart, created = Cart.objects.get_or_create(completed=False)
        self.assertEqual(cart.total_price, 400)
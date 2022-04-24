from decimal import Decimal
from shop.model import Product
from django.conf import settings


class Cart(object):

    def __init__(self, request):
        self.session = request.session
        cart = self.session.get('setting.CART_SESSION_ID')

        if not cart:
            # save an empty cart in the session
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart

    def add(self, product, quantity=1, update_quantity=False):
        """ Add or update quantity"""

        product_id = str(product.id)
        if product_url not in self.cart:
            self.cart[product_id] = {
                'quantity': 0,
                'price': str(product.price)
            }

        if update_quantity:
            self.cart[product_id]['quantity'] = quantity
        else:
            self.cart[product_id]['quantity'] += quantity
        self.save()

    def save(self):
        self.session = self.session[settings.CART_SESSION_ID] = self.cart
        self.session.modified = True


    def remove(self, product):
        """delete product from the cart"""
        product_id = str(product.id)
        if product_id in self.cart:
            del self.cart[product_id]
        self.save()
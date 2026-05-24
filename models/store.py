from dataclasses import dataclass, field


@dataclass
class Product:
    id: int
    name: str
    price: float
    stock: int

    def __str__(self):
        return f"{self.id} | {self.name} | ${self.price} | Stock: {self.stock}"


@dataclass
class CartItem:
    product: Product
    quantity: int

    def total(self):
        return self.product.price * self.quantity


class Store:
    def __init__(self):
        self.products: list[Product] = []
        self.cart: list[CartItem] = []

    # ADD PRODUCT
    def add_product(self, product: Product):
        self.products.append(product)

    # LIST PRODUCTS
    def list_products(self):
        return self.products

    # FIND PRODUCT
    def find_product(self, product_id: int):
        for p in self.products:
            if p.id == product_id:
                return p
        return None

    # ADD TO CART
    def add_to_cart(self, product_id: int, quantity: int):
        product = self.find_product(product_id)
        if not product:
            return "Product not found"

        if product.stock < quantity:
            return "Not enough stock"

        product.stock -= quantity

        # check if already in cart
        for item in self.cart:
            if item.product.id == product_id:
                item.quantity += quantity
                return "Updated cart"

        self.cart.append(CartItem(product, quantity))
        return "Added to cart"

    # VIEW CART
    def view_cart(self):
        return self.cart

    # TOTAL PRICE
    def cart_total(self):
        return sum(item.total() for item in self.cart)

    # CLEAR CART
    def clear_cart(self):
        self.cart = []

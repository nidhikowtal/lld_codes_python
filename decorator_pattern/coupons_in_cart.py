from abc import ABC, abstractmethod

# ---------- Component Interface ----------
class CartComponent(ABC):
    @abstractmethod
    def get_price(self):
        pass


# ---------- Concrete Component ----------
class BaseCart(CartComponent):
    def __init__(self, items):
        # items = [(item_name, price), ...]
        self.items = items

    def get_price(self):
        return sum(price for _, price in self.items)


# ---------- Decorator Base ----------
class CouponDecorator(CartComponent):
    def __init__(self, cart_component: CartComponent):
        self.cart_component = cart_component

    @abstractmethod
    def get_price(self):
        pass


# ---------- Concrete Decorators ----------
class FlatCoupon(CouponDecorator):
    def __init__(self, cart_component: CartComponent, discount: float):
        super().__init__(cart_component)
        self.discount = discount

    def get_price(self):
        price = self.cart_component.get_price()
        final_price = max(0, price - self.discount)
        print(f"Applied flat ₹{self.discount} off: {price} → {final_price}")
        return final_price


class PercentageCoupon(CouponDecorator):
    def __init__(self, cart_component: CartComponent, percent: float):
        super().__init__(cart_component)
        self.percent = percent

    def get_price(self):
        price = self.cart_component.get_price()
        discount = price * (self.percent / 100)
        final_price = price - discount
        print(f"Applied {self.percent}% off: {price} → {final_price}")
        return final_price



items = [("Shoes", 2000), ("Shirt", 1000), ("Jeans", 1500)]
cart = BaseCart(items)

print(f"🛒 Original price: {cart.get_price()}")

# Apply 10% discount, then ₹100 flat off
discounted_cart = FlatCoupon(PercentageCoupon(cart, 10), 100)
final_price = discounted_cart.get_price()

print(f"💰 Final payable amount: ₹{final_price}")

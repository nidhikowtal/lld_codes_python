class Product:
    def __init__(self, name: str, quantity: int):
        self.name = name
        self.quantity = quantity

    def reduce_stock(self, amount: int):
        if amount <= self.quantity:
            self.quantity -= amount
        else:
            raise ValueError("Not enough stock available!")

    def is_out_of_stock(self) -> bool:
        return self.quantity == 0

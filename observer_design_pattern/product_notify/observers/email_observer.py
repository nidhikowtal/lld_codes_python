from interfaces.observer import Observer

class EmailObserver(Observer):
    def __init__(self, email: str):
        self.email = email

    def update(self, product_name: str):
        print(f"[EMAIL] Sent to {self.email}: '{product_name}' is now OUT OF STOCK!")

from interfaces.observer import Observer

class SMSObserver(Observer):
    def __init__(self, phone: str):
        self.phone = phone

    def update(self, product_name: str):
        print(f"[SMS] Sent to {self.phone}: '{product_name}' is now OUT OF STOCK!")

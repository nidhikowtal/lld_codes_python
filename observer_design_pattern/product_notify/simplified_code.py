from abc import ABC, abstractmethod

# --- Observer Interface ---
class Observer(ABC):
    @abstractmethod
    def update(self, message):
        pass

# --- Subject Interface ---
class Subject(ABC):
    @abstractmethod
    def add_observer(self, observer):
        pass

    @abstractmethod
    def remove_observer(self, observer):
        pass

    @abstractmethod
    def notify_observers(self, message):
        pass

# --- Concrete Subject (Product) ---
class Product(Subject):
    def __init__(self, name):
        self.name = name
        self.observers = []
        self.in_stock = False

    def add_observer(self, observer):
        self.observers.append(observer)

    def remove_observer(self, observer):
        self.observers.remove(observer)

    def set_in_stock(self, in_stock):
        self.in_stock = in_stock
        status=""
        if in_stock:
            status = "available" 
        else:
            status = "out of stock"
        print(f"\n[Product Update] {self.name} is now {status}.")
        self.notify_observers(f"{self.name} is now {status}!")

    def notify_observers(self, message):
        for observer in self.observers:
            observer.update(message)

# --- Concrete Observers ---
class EmailSubscriber(Observer):
    def __init__(self, email: str):
        self.email = email

    def update(self, message):
        print(f"📧 Email sent to {self.email}: {message}")

class SMSSubscriber(Observer):
    def __init__(self, phone):
        self.phone = phone

    def update(self, message):
        print(f"📱 SMS sent to {self.phone}: {message}")

# --- Client Code ---
# Create product (subject)
laptop = Product("MacBook")

# Create observers (subscribers)
email = EmailSubscriber("nidhi@example.com")
sms = SMSSubscriber("+91-9876543210")

# Register observers
laptop.add_observer(email)
laptop.add_observer(sms)

# Change product stock status
laptop.set_in_stock(True)
laptop.set_in_stock(False)

# Unsubscribe one user
laptop.remove_observer(sms)

# Restock product
laptop.set_in_stock(True)

from interfaces.subject import Subject

class InventoryService(Subject):
    def __init__(self):
        self._observers = []

    def add_observer(self, observer):
        self._observers.append(observer)

    def remove_observer(self, observer):
        self._observers.remove(observer)

    def notify_observers(self, product_name: str):
        for observer in self._observers:
            observer.update(product_name)

    def check_and_notify(self, product):
        if product.is_out_of_stock():
            self.notify_observers(product.name)

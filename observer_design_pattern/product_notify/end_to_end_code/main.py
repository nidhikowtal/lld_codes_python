from entities.product import Product
from observers.email_observer import EmailObserver
from observers.sms_observer import SMSObserver
from services.inventory_service import InventoryService

if __name__ == "__main__":
    laptop = Product("Laptop", 2)
    inventory_service = InventoryService()
    inventory_service.add_observer(EmailObserver("user@example.com"))
    inventory_service.add_observer(SMSObserver("+91-9876543210"))

    laptop.reduce_stock(1)
    inventory_service.check_and_notify(laptop)

    laptop.reduce_stock(1)
    inventory_service.check_and_notify(laptop)

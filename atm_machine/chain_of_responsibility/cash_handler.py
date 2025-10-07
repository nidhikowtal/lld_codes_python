class CashHandler:
    def __init__(self, denomination, count):
        self.denomination = denomination
        self.count = count
        self.next_handler = None

    def set_next(self, handler):
        self.next_handler = handler
        return handler

    def withdraw(self, amount):
        notes_needed = min(amount // self.denomination, self.count)
        self.count -= notes_needed
        amount_left = amount - notes_needed * self.denomination

        if notes_needed > 0:
            print(f"✅ Dispensed {notes_needed} x ₹{self.denomination} notes")

        if amount_left > 0:
            if self.next_handler:
                return self.next_handler.withdraw(amount_left)
            else:
                # If last handler can't dispense remaining amount
                return amount_left
        return 0  # fully dispensed

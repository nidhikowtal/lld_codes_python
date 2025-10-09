from atm_state import ATMState

class IdleState(ATMState):
    def insert_card(self, atm):
        print("✅ Card inserted.")
        atm.set_state(atm.has_card_state)

    def authenticate_pin(self, atm, card, pin): 
        print("⚠️ Insert card first.")

    def select_operation(self, atm, operation): 
        print("⚠️ Insert card first.")

    def withdraw_cash(self, atm, amount): 
        print("⚠️ Insert card first.")


class HasCardState(ATMState):
    def insert_card(self, atm): 
        print("⚠️ Card already inserted.")

    def authenticate_pin(self, atm, card, pin):
        if card.pin == pin:
            print("✅ PIN verified successfully.")
            atm.set_state(atm.select_operation_state)
        else:
            print("❌ Invalid PIN. Card ejected.")
            atm.set_state(atm.idle_state)

    def select_operation(self, atm, operation): 
        print("⚠️ Authenticate PIN first.")

    def withdraw_cash(self, atm, amount): 
        print("⚠️ Authenticate PIN first.")


class SelectOperationState(ATMState):
    def insert_card(self, atm): 
        print("⚠️ Card already inserted.")

    def authenticate_pin(self, atm, card, pin): 
        print("⚠️ PIN already verified.")

    def select_operation(self, atm, operation):
        if operation == "WITHDRAW":
            print("💰 Withdrawal selected.")
            atm.set_state(atm.cash_withdraw_state)
        elif operation == "BALANCE":
            print(f"💳 Current balance: ₹{atm.balance}")
            atm.set_state(atm.idle_state)
        else:
            print("⚠️ Unsupported operation.")
            atm.set_state(atm.idle_state)

    def withdraw_cash(self, atm, amount): 
        print("⚠️ Select operation first.")


class CashWithdrawState(ATMState):
    def insert_card(self, atm): 
        print("⚠️ Transaction in progress. Please wait.")

    def authenticate_pin(self, atm, card, pin): 
        print("⚠️ Transaction in progress. Please wait.")

    def select_operation(self, atm, operation): 
        print("⚠️ Transaction in progress. Please wait.")
        
    def withdraw_cash(self, atm, amount):
        if atm.balance >= amount:
            atm.balance -= amount
            print(f"✅ Dispensed ₹{amount}. Remaining balance: ₹{atm.balance}")
        else:
            print("❌ Insufficient funds.")

        print("💳 Please collect your card.")
        atm.set_state(atm.idle_state)


class ATM:
    def __init__(self, initial_balance=0):
        self.idle_state = IdleState()
        self.has_card_state = HasCardState()
        self.select_operation_state = SelectOperationState()
        self.cash_withdraw_state = CashWithdrawState()

        self.state = self.idle_state
        self.balance = initial_balance

    def set_state(self, new_state):
        self.state = new_state

    def get_state(self):
        return self.state

from atm_state import ATMState
from cash_handler import CashHandler

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
            print(f"💰 Attempting to withdraw ₹{amount}...")
            remaining = atm.two_thousand_notes.withdraw(amount)
            if remaining == 0:
                atm.balance -= amount
                print(f"✅ Withdrawal successful. Remaining balance: ₹{atm.balance}")
            else:
                print("❌ Withdrawal failed due to insufficient notes.")
        else:
            print("❌ Insufficient funds.")

        print("💳 Please collect your card.")
        atm.set_state(atm.idle_state)



class ATM:
    def __init__(self):
        # Existing states
        self.idle_state = IdleState()
        self.has_card_state = HasCardState()
        self.select_operation_state = SelectOperationState()
        self.cash_withdraw_state = CashWithdrawState()

        self.state = self.idle_state

        # Initialize note handlers (Chain of Responsibility)
        self.two_thousand_notes = CashHandler(2000, 5)  # example counts
        self.one_thousand_notes = CashHandler(1000, 10)

        # chain: 2k -> 1k
        self.two_thousand_notes.set_next(self.one_thousand_notes)

        self.balance = (self.two_thousand_notes.count * 2000) + (self.one_thousand_notes.count * 1000)

    def set_state(self, new_state):
        self.state = new_state

    def get_state(self):
        return self.state

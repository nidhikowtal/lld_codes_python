from atm import ATM

class Card:
    def __init__(self, pin): 
        self.pin = pin


card = Card(pin=1234)
atm = ATM(initial_balance=10000)

atm.get_state().insert_card(atm)
atm.get_state().authenticate_pin(atm, card, 1234)
atm.get_state().select_operation(atm, "WITHDRAW")
atm.get_state().withdraw_cash(atm, 15000)

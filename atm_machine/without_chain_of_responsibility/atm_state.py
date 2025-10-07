from abc import ABC, abstractmethod

class ATMState(ABC):
    @abstractmethod
    def insert_card(self, atm): pass

    @abstractmethod
    def authenticate_pin(self, atm, card, pin): pass

    @abstractmethod
    def select_operation(self, atm, operation): pass

    @abstractmethod
    def withdraw_cash(self, atm, amount): pass

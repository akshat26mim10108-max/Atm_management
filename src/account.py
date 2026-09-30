# Account data and basic account operations

class Account:
    def __init__(self, pin, balance):
        self.pin = pin
        self.balance = balance

    def check_pin(self, entered_pin):
        return entered_pin == self.pin

    def change_pin(self, old_pin, new_pin):
        if old_pin == self.pin:
            self.pin = new_pin
            return True
        return False

    def add_money(self, amount):
        self.balance += amount

    def remove_money(self, amount):
        self.balance -= amount

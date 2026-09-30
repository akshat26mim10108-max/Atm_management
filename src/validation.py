# Input validation helpers

def positive_amount(amount):
    return amount > 0

def valid_pin(pin):
    return 1000 <= pin <= 9999

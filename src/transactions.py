# Transaction history

class TransactionHistory:
    def __init__(self):
        self.items = []

    def add(self, text):
        self.items.append(text)

    def show(self):
        if not self.items:
            print("No transactions yet.")
            return

        for number, item in enumerate(self.items, 1):
            print(f"{number}. {item}")

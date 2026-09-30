# Main ATM operations

from validation import positive_amount, valid_pin

def deposit_money(account, history):
    print("\n----- DEPOSIT MONEY -----")
    try:
        amount = float(input("Enter amount: Rs. "))

        if not positive_amount(amount):
            print("Please enter a valid amount.")
            return

        account.add_money(amount)
        history.add(f"Deposited Rs. {amount:.2f}")
        print("Money deposited successfully.")

    except ValueError:
        print("Please enter a number.")


def withdraw_money(account, history):
    print("\n----- WITHDRAW MONEY -----")
    try:
        amount = float(input("Enter amount: Rs. "))

        if not positive_amount(amount):
            print("Please enter a valid amount.")
        elif amount > account.balance:
            print("Insufficient balance.")
        else:
            account.remove_money(amount)
            history.add(f"Withdrawn Rs. {amount:.2f}")
            print("Please collect your money.")

    except ValueError:
        print("Please enter a number.")


def change_pin(account):
    print("\n----- CHANGE PIN -----")

    try:
        old_pin = int(input("Enter old PIN: "))

        if not account.check_pin(old_pin):
            print("Wrong old PIN.")
            return

        new_pin = int(input("Enter new 4-digit PIN: "))

        if not valid_pin(new_pin):
            print("PIN must contain 4 digits.")
            return

        account.pin = new_pin
        print("PIN changed successfully.")

    except ValueError:
        print("PIN must contain numbers only.")

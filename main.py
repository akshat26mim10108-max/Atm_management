# ATM Management System
# Entry point of the project

from config import STARTING_BALANCE, DEFAULT_PIN
from account import Account
from transactions import TransactionHistory
from operations import deposit_money, withdraw_money, change_pin
from menu import show_menu


def main():
    account = Account(DEFAULT_PIN, STARTING_BALANCE)
    history = TransactionHistory()

    print("===== WELCOME TO ATM =====")

    try:
        entered_pin = int(input("Enter your PIN: "))
    except ValueError:
        print("Invalid PIN.")
        return

    if not account.check_pin(entered_pin):
        print("Wrong PIN.")
        return

    while True:
        choice = show_menu()

        if choice == "1":
            print("\n----- BALANCE -----")
            print("Your balance is: Rs.", account.balance)

        elif choice == "2":
            deposit_money(account, history)

        elif choice == "3":
            withdraw_money(account, history)

        elif choice == "4":
            print("\n----- TRANSACTION HISTORY -----")
            history.show()

        elif choice == "5":
            change_pin(account)

        elif choice == "6":
            print("Thank you for using ATM.")
            break

        else:
            print("Please select a valid option.")


if __name__ == "__main__":
    main()

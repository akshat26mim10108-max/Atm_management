import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parents[1] / "src"))

from account import Account
from transactions import TransactionHistory
from validation import positive_amount, valid_pin


def test_pin():
    account = Account(1234, 5000)
    assert account.check_pin(1234)
    assert not account.check_pin(1111)


def test_deposit():
    account = Account(1234, 5000)
    account.add_money(500)
    assert account.balance == 5500


def test_withdraw():
    account = Account(1234, 5000)
    account.remove_money(1000)
    assert account.balance == 4000


def test_validation():
    assert positive_amount(10)
    assert not positive_amount(0)
    assert valid_pin(1234)
    assert not valid_pin(12)


def test_history():
    history = TransactionHistory()
    history.add("Deposited Rs. 100")
    assert len(history.items) == 1

from unittest.mock import Mock
from bank import BankAccount
import pytest

@pytest.fixture()
def account():
    return BankAccount("Deepan",1000)

def test_deposit(account):
     assert account.deposit(500) == 1500

def test_withdraw(account):
    assert account.withdraw(500) == 500

def test_withdraw_insufficient_balance(account):
    with pytest.raises(ValueError):
        account.withdraw(1001)


def test_deposit_invalid_amount(account):
    with pytest.raises(ValueError):
        account.deposit(-500)

def test_deposit_notification(account):
    notification = Mock()
    account.deposit(500,notification)
    notification.send.assert_called_once()
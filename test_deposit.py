import pytest
from bank import BankAccount

# setup fixture for bank account
@pytest.fixture
def account():
    return BankAccount(balance=100)

# successful deposit test
def test_deposit_increases_balance(account):
    account.deposit(50)
    assert account.balance == 150

# deposit returns the new balance
def test_deposit_returns_new_balance(account):
    result = account.deposit(30)
    assert result == 130
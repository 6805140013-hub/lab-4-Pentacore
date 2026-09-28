import pytest
from bank import BankAccount

##setup fixture for bank account
@pytest.fixture
def account():
    return BankAccount(balance=100)

##successful withdraw test
def test_withdraw_decreases_balance(account):
    account.withdraw(50)
    assert account.balance == 50

##value error test
def test_withdraw_overdraw_raises_error(account):
    with pytest.raises(ValueError):
        account.withdraw(150)
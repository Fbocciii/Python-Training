#from Python_Testing.Pytest import Account
from Account import Accounts
import pytest


def test_create_positive():
    account = Accounts("John", 100)
    assert account.acclist.get("John") is not None and account.acclist["John"] == 100


def test_create_negative():
    with pytest.raises(Exception) as excep:
        account = Accounts("John", -50)
    assert str(excep.value) == "Overdraft on John"


def test_add_acc_positive():
    account = Accounts("John", 100)
    account.newacct("Jane")
    assert account.acclist.get("Jane") is not None and account.acclist["Jane"] == 0


def test_add_acc_negative():
    account = Accounts("John", 100)
    with pytest.raises(Exception) as excep:
        account.newacct("John")
    assert str(excep.value) == "'Account name John already exists.'"

@pytest.mark.parametrize("frm,to,amt",
                        [("John", "Beth", 10),
                         ("Jake", "Jess", 30),
                         ("Mike", "April", 40)]
                        )
def test_transfer_positive(frm, to, amt):
    account = Accounts(frm, 100)
    account.newacct(to)

    prevFrm = account.value(frm)
    prevTo = account.value(to)
    account.transfer(frm, to, amt)
    assert prevFrm - amt == account.value(frm) and prevTo + amt == account.value(to)


@pytest.mark.parametrize("frm,to,amt",
                         [("John", "Beth", 100),
                          ("Jake", "Jess", 30),
                          ("Mike", "April", 40)]
                         )
def test_transfer_negative(frm, to, amt):
    accounts = Accounts(frm, 10)
    with pytest.raises(Exception) as excep:
        accounts.transfer(frm, to, amt)

    assert str(excep.value) == ("Overdraft on " + frm)


def test_close_account_empty():
    account = Accounts("John", 0)
    account.close("John")

    with pytest.raises(Exception) as excep:
        account.value("John")
    assert excep.type == KeyError

def test_close_account_not_empty():
    account = Accounts("John", 1)

    with pytest.raises(Exception) as excep:
        account.close("John")

    assert str(excep.value) == "Close of non-empty John"

@pytest.mark.parametrize("acc_name,amt",
                         [("A", 20),
                          ("B", 50),
                          ("C", 100)]
                         )
def test_close_account_transfer(acc_name, amt):
    account = Accounts("John", 20)
    account.acclist[acc_name] = amt

    account.close(acc_name, "John")
    assert account.value("John") == 20 + amt




if __name__ == "__main__":
    pytest.main()
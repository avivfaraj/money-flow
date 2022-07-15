from flow.src.bank_account import Bank_Account
import pytest


b1 = Bank_Account(1, "Charles Schwab", 10000)
b2 = Bank_Account(2, "Capital One", 5000)


class TestBank_Account():

    # Sucessful test
    def test_ID(self):
        assert b1.ID == 1
        assert b2.ID == 2

    def test_name(self):
        assert b1.name == "Charles Schwab"
        assert b2.name == "Capital One"

    def test_balance(self):
        assert b1.balance == 10000
        assert b2.balance == 5000

    def test_transactions(self):
        assert b1.transactions == []
        assert b2.transactions == []

    def test_update_balance(self):
        # Income - balance goes up
        b1.update_balance(100, True)
        b2.update_balance(200, True)

        # Test that it actually went up
        assert b1.balance == 10100
        assert b2.balance == 5200

        # Expense - balance goes down
        b1.update_balance(200, False)
        b2.update_balance(100)

        # Test that it actually went up
        assert b1.balance == 9900
        assert b2.balance == 5100


    # Failed tests 
    def test_ID_failure(self):
        """ Make sure an invalid ID raises a value error exception """
        with pytest.raises(ValueError) as excinfo:
            _ = Bank_Account(name = "Capital One", balance = 5000)

        exception_msg = excinfo.value.args[0]
        assert exception_msg == "ID must be positive"

        with pytest.raises(ValueError) as excinfo:
            _ = Bank_Account(name = "Capital One", balance = 5000)

        exception_msg = excinfo.value.args[0]
        assert exception_msg == "ID must be positive"

    def test_name_failure(self):
        """ Make sure an invalid bank's name raises exceptions """

        # Name is empty
        with pytest.raises(ValueError) as excinfo:
            _ = Bank_Account(3, balance = 3000)

        exception_msg = excinfo.value.args[0]
        assert exception_msg == "Name was empty"

        # Name is not string
        with pytest.raises(TypeError) as excinfo:
            _ = Bank_Account(3, name = 4, balance = 400)

        exception_msg = excinfo.value.args[0]
        assert exception_msg == "Name must be a string"

    def test_balance_failure(self):
        """ Make sure an invalid balance raises exceptions """

        # Balance is empty
        with pytest.raises(TypeError) as excinfo:
            _ = Bank_Account(3, name = "test")

        exception_msg = excinfo.value.args[0]
        assert exception_msg == "Balance must be either an integer or float"

        # Balance is str (neither int nor float)
        with pytest.raises(TypeError) as excinfo:
            _ = Bank_Account(3, name = "test", balance = "444")

        exception_msg = excinfo.value.args[0]
        assert exception_msg == "Balance must be either an integer or float"

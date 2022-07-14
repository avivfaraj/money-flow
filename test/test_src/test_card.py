from flow.src.card import Card
import pytest


c1 = Card(4444, "VISA", 123)
c2 = Card(2134, "American Express", 4442)


class TestCard():

    # Sucessful test
    def test_ID(self):
        assert c1.ID == 4444
        assert c2.ID == 2134

    def test_company(self):
        assert c1.company == "VISA"
        assert c2.company == "American Express"

    def test_account_num(self):
        assert c1.account_num == 123
        assert c2.account_num == 4442


    # Failed tests 
    def test_ID_failure(self):
        """ Make sure an invalid ID raises a value error exception """
        
        # Case 1 - ID is not int (str)
        with pytest.raises(ValueError) as excinfo:
            _ = Card("4444", "VISA", 123)

        exception_msg = excinfo.value.args[0]
        assert exception_msg == "ID is not valid"

        # Case 2 - ID is int, but negative
        with pytest.raises(ValueError) as excinfo:
            _ = Card(-4, "VISA", 123)

        exception_msg = excinfo.value.args[0]
        assert exception_msg == "ID is not valid"

        # Case 3 - ID is int, positive, but its length is not 4
        with pytest.raises(ValueError) as excinfo:
            _ = Card(123, "VISA", 123)

        # Case 4 - ID is missing
        with pytest.raises(NotImplementedError) as excinfo:
            _ = Card(company = "VISA", account_num = 123)

        exception_msg = excinfo.value.args[0]
        assert exception_msg == "ID is required"

    def test_company_failure(self):
        """ Make sure an invalid company name raises an exception """

        # Company name is empty
        with pytest.raises(ValueError) as excinfo:
            _ = Card(4444, account_num = 123)

        exception_msg = excinfo.value.args[0]
        assert exception_msg == "Card Company is missing!"

    def test_account_num_failure(self):
        """ Make sure an invalid account number raises exceptions """

        # Account number is empty
        with pytest.raises(ValueError) as excinfo:
            _ = Card(1234, "VISA")

        exception_msg = excinfo.value.args[0]
        assert exception_msg == "Account Number is None. It must be an integer"

        # Account number is not int (str)
        with pytest.raises(TypeError) as excinfo:
            _ = Card(1234, "VISA", "1234")

        exception_msg = excinfo.value.args[0]
        assert exception_msg == "Account Number must be an integer"

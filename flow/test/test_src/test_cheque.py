from flow.src.cheque import Cheque
import pytest


c1 = Cheque(4444, "Charles Schwab", 123, "Michael McHill", "Maintenance")
c2 = Cheque(2134, "Truist", 4442, "Garden Club", "Membership")


class TestCheque():

    # Sucessful test
    def test_ID(self):
        assert c1.ID == 4444
        assert c2.ID == 2134

    def test_company(self):
        assert c1.company == "Charles Schwab"
        assert c2.company == "Truist"

    def test_account_num(self):
        assert c1.account_num == 123
        assert c2.account_num == 4442

    def test_pay_to(self):
        assert c1.pay_to == 'Michael McHill'
        assert c2.pay_to == "Garden Club"

    def test_memo(self):
        assert c1.memo == "Maintenance"
        assert c2.memo == "Membership"


    # Failed tests 
    def test_ID_failure(self):
        """ Make sure an invalid ID raises a value error exception """
        
        # Case 1 - ID is not int (str)
        with pytest.raises(ValueError) as excinfo:
            c1.ID = "444"

        exception_msg = excinfo.value.args[0]
        assert exception_msg == "ID is not valid"

        # Case 2 - ID is int, but negative
        with pytest.raises(ValueError) as excinfo:
            c1.ID = -1

        exception_msg = excinfo.value.args[0]
        assert exception_msg == "ID is not valid"

        # Case 3 - ID is int, positive, but its length is not 4
        with pytest.raises(ValueError) as excinfo:
            c1.ID = 23

        # Case 4 - ID is missing
        with pytest.raises(NotImplementedError) as excinfo:
            _ = Cheque(company = "Charles Schwab",
                       account_num = 123,
                       pt = "Michael McHill",
                       memo = "Maintenance")

        exception_msg = excinfo.value.args[0]
        assert exception_msg == "ID is required"

    def test_company_failure(self):
        """ Make sure an invalid company name raises an exception """

        # Company name is empty
        with pytest.raises(ValueError) as excinfo:
            _ = Cheque(id_ = 4444,
                       account_num = 123,
                       pt = "Michael McHill",
                       memo = "Maintenance")

        exception_msg = excinfo.value.args[0]
        assert exception_msg == "Company is missing!"

    def test_account_num_failure(self):
        """ Make sure an invalid account number raises exceptions """

        # Account number is empty
        with pytest.raises(ValueError) as excinfo:
            _ = Cheque(id_ = 4444,
                       company = "Charles Schwab",
                       pt = "Michael McHill",
                       memo = "Maintenance")

        exception_msg = excinfo.value.args[0]
        assert exception_msg == "Account Number is None. It must be an integer"

        # Account number is not int (str)
        with pytest.raises(TypeError) as excinfo:
            _ = Cheque(id_ = 4444,
                       company = "Charles Schwab",
                       account_num = "444",
                       pt = "Michael McHill",
                       memo = "Maintenance")

        exception_msg = excinfo.value.args[0]
        assert exception_msg == "Account Number must be an integer"

    def test_pay_to_failure(self):
        """ Make sure an invalid account number raises exceptions """

        # pay_to is empty
        with pytest.raises(ValueError) as excinfo:
            _ = Cheque(id_ = 4444,
                       company = "Charles Schwab",
                       account_num = 1234,
                       memo = "Maintenance")

        exception_msg = excinfo.value.args[0]
        assert exception_msg == "Pay To is missing!"

        # Account number is not str (list)
        with pytest.raises(TypeError) as excinfo:
            _ = Cheque(id_ = 4444,
                       company = "Charles Schwab",
                       account_num = 1234,
                       pt = [1,23],
                       memo = "Maintenance")

        exception_msg = excinfo.value.args[0]
        assert exception_msg == "Pay To must be a string"

    def test_memo_failure(self):
        """ Make sure an invalid account number raises exceptions """

        # memo is empty
        with pytest.raises(ValueError) as excinfo:
            _ = Cheque(id_ = 4444,
                       company = "Charles Schwab",
                       account_num = 1234,
                       pt = "Maintenance")

        exception_msg = excinfo.value.args[0]
        assert exception_msg == "Memo is missing!"

        # Account number is not str (list)
        with pytest.raises(TypeError) as excinfo:
            _ = Cheque(id_ = 4444,
                       company = "Charles Schwab",
                       account_num = 1234,
                       pt = "Maintenace",
                       memo = [1,23])

        exception_msg = excinfo.value.args[0]
        assert exception_msg == "Memo must be a string"


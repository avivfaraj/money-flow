from flow.src.deposit import Deposit
from flow.src.wire_transfer import Wire
from flow.src.cheque import Cheque
from datetime import datetime as dt
import pytest

date_ = dt.now()
w = Wire(4010, 
         "Bank of America", 
         4111,
         "Myself",
         "Work",
         "Domestic",
         "Salary")

ch = Cheque(4010, "Bank of America", 4111, "School", "Refund")

d1 = Deposit(4444,
             "Income",
             14000.1,
             payment = w)

d2 = Deposit(2134,
             "Refund from school",
             4442,
             dt(2021, 2, 10),
             ch)

class TestDeposit():

    # Sucessful test
    def test_ID(self):
        assert d1.ID == 4444
        assert d2.ID == 2134

    def test_details(self):
        assert d1.details == "Income"
        assert d2.details == "Refund from school"

    def test_date(self):
        assert d1.date_str() == date_.strftime("%d/%m/%Y")
        assert d1.time_str() == date_.strftime("%-I:%M %p")
        assert d2.date_str() == dt(2021, 2, 10).strftime("%d/%m/%Y")
        assert d2.time_str() == dt(2021, 2, 10).strftime("%-I:%M %p")

    def test_payment(self):
        assert d1.payment == w
        assert d2.payment == ch

    # Failed tests 
    def test_total_failure(self):
        """ Make sure an invalid total raises a value error exception """
        
        # Case 1 - Total is negative
        with pytest.raises(ValueError) as excinfo:
            d1.total = -5

        exception_msg = excinfo.value.args[0]
        assert exception_msg == "Deposit must be positive"

        # Case 2 - total is string
        with pytest.raises(TypeError) as excinfo:
            d2.total = "Testing string"

        exception_msg = excinfo.value.args[0]
        assert exception_msg == "Deposit must be a number"

        # Case 3 - Deposit is a list
        with pytest.raises(TypeError) as excinfo:
            d2.total = [1, 2, 4.5]

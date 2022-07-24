from flow.src.withdrawal import Withdrawal
from flow.src.wire_transfer import Wire
from flow.src.cheque import Cheque
from flow.src.card import Card
from datetime import datetime as dt
import pytest


date_ = dt.now()
c = Card(4444, "VISA", 123)
ch = Cheque(4010, "Bank of America", 4111, "Bike shop", "Shoes")

w1 = Withdrawal(ID = 1,
                details = "T-shirt CK",
                unit_price = 2,
                amount = 5,
                sector = "Fashion",
                payment = c,
                discount = 2)

w2 = Withdrawal(ID = 2,
                details = "Bike shoes",
                date = dt(2021, 2,4,5,6),
                unit_price = 100,
                amount = 1,
                sector = "Sport",
                payment = ch,
                discount = 0)

class TestDeposit():

    # Sucessful test
    def test_ID(self):
        assert w1.ID == 1
        assert w2.ID == 2

    def test_details(self):
        assert w1.details == "T-shirt CK"
        assert w2.details == "Bike shoes"

    def test_date(self):
        assert w1.date_str() == date_.strftime("%d/%m/%Y")
        assert w1.time_str() == date_.strftime("%-I:%M %p")
        assert w2.date_str() == dt(2021, 2,4,5,6).strftime("%d/%m/%Y")
        assert w2.time_str() == dt(2021, 2,4,5,6).strftime("%-I:%M %p")

    def test_unit_price(self):
        assert w1.unit_price == 2
        assert w2.unit_price == 100

    def test_amount(self):
        assert w1.amount == 5
        assert w2.amount == 1

    def test_sector(self):
        assert w1.sector == "Fashion"
        assert w2.sector == "Sport"

    def test_discount(self):
        assert w1.discount == 2
        assert w2.discount == 0

    def test_total(self):
        assert w1.total == 8
        assert w2.total == 100
    
    # Failed tests 
    def test_unit_price_failure(self):
        """ Make sure an invalid price raises a value error exception """
        
        # Case 1 - price is negative
        with pytest.raises(ValueError) as excinfo:
            w1.unit_price = -5

        exception_msg = excinfo.value.args[0]
        assert exception_msg == "Price Must be Positive"

        # Case 2 - price is string
        with pytest.raises(TypeError) as excinfo:
            w2.unit_price = "Testing string"

        exception_msg = excinfo.value.args[0]
        assert exception_msg == "Price must be either an iteger or float"

    def test_amount_failure(self):
        """ Make sure an invalid amount raises a value error exception """
        
        # Case 1 - amount is negative
        with pytest.raises(ValueError) as excinfo:
            w1.amount = -5

        exception_msg = excinfo.value.args[0]
        assert exception_msg == "Amount Must be Positive"

        # Case 2 - amount is string
        with pytest.raises(TypeError) as excinfo:
            w2.amount = "Testing string"

        exception_msg = excinfo.value.args[0]
        assert exception_msg == "Amount must be either an iteger or float"

    def test_sector_failure(self):
        """ Make sure an invalid sector raises a value error exception """
        
        with pytest.raises(TypeError) as excinfo:
            w1.sector = -5

        exception_msg = excinfo.value.args[0]
        assert exception_msg == "Sector must be a string"

    def test_payment_failure(self):
        """ Make sure an invalid payment raises a value error exception """
        
        # Case 1 - Missing 
        with pytest.raises(ValueError) as excinfo:
            w1.payment = None

        exception_msg = excinfo.value.args[0]
        assert exception_msg == "Payment is missing!"

        # Case 2 - Payment is a string 
        with pytest.raises(TypeError) as excinfo:
            w2.payment = "Another type of payment - invalid"

        exception_msg = excinfo.value.args[0]
        assert exception_msg == "Valid payments type: Card, Cheque and Wire"

    def test_discount_failure(self):
        """ Make sure an invalid discount raises a value error exception """
        
        with pytest.raises(TypeError) as excinfo:
            w1.discount = "String"

        exception_msg = excinfo.value.args[0]
        assert exception_msg == "Discount must be a number"


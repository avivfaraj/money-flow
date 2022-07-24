from flow.src.wire_transfer import Wire
import pytest


w1 = Wire(4444,
          "Charles Schwab",
          123,
          "Michael McHill",
          "Tom Press",
          "Domestic",
          "Testing a domestic wire transfer")

w2 = Wire(2134,
          "Truist",
          4442,
          "Tim Hanks",
          "Lavander George",
          "International",
          "Testing an international wire transfer")

class TestWire():

    # Sucessful test
    def test_ID(self):
        assert w1.ID == 4444
        assert w2.ID == 2134

    def test_company(self):
        assert w1.company == "Charles Schwab"
        assert w2.company == "Truist"

    def test_account_num(self):
        assert w1.account_num == 123
        assert w2.account_num == 4442

    def test_recipient(self):
        assert w1.recipient == 'Michael McHill'
        assert w2.recipient == "Tim Hanks"

    def test_sender(self):
        assert w1.sender == "Tom Press"
        assert w2.sender == "Lavander George"

    def test_wire_type(self):
        assert w1.w_type == "Domestic"
        assert w2.w_type == "International"

    def test_details(self):
        assert w1.details == "Testing a domestic wire transfer"
        assert w2.details == "Testing an international wire transfer"

    # Failed tests 
    def test_ID_failure(self):
        """ Make sure an invalid ID raises a value error exception """
        
        # Case 1 - ID is not int (str)
        with pytest.raises(ValueError) as excinfo:
            w1.ID = "444"

        exception_msg = excinfo.value.args[0]
        assert exception_msg == "ID is not valid"

        # Case 2 - ID is int, but negative
        with pytest.raises(ValueError) as excinfo:
            w1.ID = -1

        exception_msg = excinfo.value.args[0]
        assert exception_msg == "ID is not valid"

        # Case 3 - ID is int, positive, but its length is not 4
        with pytest.raises(ValueError) as excinfo:
            w2.ID = 23

        # Case 4 - ID is missing
        with pytest.raises(NotImplementedError) as excinfo:
            w2.ID = None

        exception_msg = excinfo.value.args[0]
        assert exception_msg == "ID is required"

    def test_company_failure(self):
        """ Make sure an invalid company name raises an exception """

        # Company name is empty
        with pytest.raises(ValueError) as excinfo:
            w1.company = None

        exception_msg = excinfo.value.args[0]
        assert exception_msg == "Company is missing!"

    def test_account_num_failure(self):
        """ Make sure an invalid account number raises exceptions """

        # Account number is empty
        with pytest.raises(ValueError) as excinfo:
            w2.account_num = None

        exception_msg = excinfo.value.args[0]
        assert exception_msg == "Account Number is None. It must be an integer"

        # Account number is not int (str)
        with pytest.raises(TypeError) as excinfo:
            w2.account_num = "5552"

        exception_msg = excinfo.value.args[0]
        assert exception_msg == "Account Number must be an integer"

    def test_recipient_failure(self):
        """ Make sure an invalid recipient raises exceptions """

        # recipient is empty
        with pytest.raises(ValueError) as excinfo:
            w2.recipient = ""

        exception_msg = excinfo.value.args[0]
        assert exception_msg == "Recipient is missing!"

        # recipient is not str (list)
        with pytest.raises(TypeError) as excinfo:
            w1.recipient = ["a", "b"]

        exception_msg = excinfo.value.args[0]
        assert exception_msg == "Recipient must be a string"

    def test_sender_failure(self):
        """ Make sure an invalid sender raises exceptions """

        # sender is empty
        with pytest.raises(ValueError) as excinfo:
            w2.sender = ""

        exception_msg = excinfo.value.args[0]
        assert exception_msg == "Sender is missing!"

        # sender is not str (int)
        with pytest.raises(TypeError) as excinfo:
            w1.sender = 123

        exception_msg = excinfo.value.args[0]
        assert exception_msg == "Sender must be a string"

    def test_wire_type_failure(self):
        """ Make sure an invalid type raises exceptions """

        # type is empty
        with pytest.raises(ValueError) as excinfo:
            w2.w_type = ""

        exception_msg = excinfo.value.args[0]
        assert exception_msg == "Type is missing!"

        # type is not str (int)
        with pytest.raises(TypeError) as excinfo:
            w1.w_type = 123

        exception_msg = excinfo.value.args[0]
        assert exception_msg == "Type must be a string"

    def test_details_failure(self):
        """ Make sure invalid details raises exceptions """

        # details is empty
        with pytest.raises(ValueError) as excinfo:
            w2.details = ""

        exception_msg = excinfo.value.args[0]
        assert exception_msg == "details is missing!"

        # details is not str (int)
        with pytest.raises(TypeError) as excinfo:
            w1.details = 123

        exception_msg = excinfo.value.args[0]
        assert exception_msg == "details must be a string"
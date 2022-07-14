from flow.src.person import Person
import pytest


p1 = Person(1, "Aviv", last_name = "Farag")
p2 = Person(2, "Jason", "Matthew", "Holmes")


class TestPerson():

    # Sucessful test
    def test_ID(self):
        assert p1.ID == 1
        assert p2.ID == 2

    def test_first_name(self):
        assert p1.first_name == "Aviv"
        assert p2.first_name == "Jason"

    def test_middle_name(self):
        assert p1.middle_name == ""
        assert p2.middle_name == "Matthew"

    def test_accounts(self):
        assert p1.accounts == []
        assert p2.accounts == []


    # Failed tests 
    def test_ID_failure(self):
        """ Make sure an invalid ID raises a value error exception """
        with pytest.raises(ValueError) as excinfo:
            _ = Person(first_name = "Aviv", last_name = "Farag")

        exception_msg = excinfo.value.args[0]
        assert exception_msg == "ID must be positive"

    def test_first_name_failure(self):
        """ Make sure an invalid first name raises exceptions """

        # First name is empty
        with pytest.raises(ValueError) as excinfo:
            _ = Person(3, last_name = "Farag")

        exception_msg = excinfo.value.args[0]
        assert exception_msg == "Name was empty"

        # First name is not string
        with pytest.raises(TypeError) as excinfo:
            _ = Person(3,first_name = 4, last_name = "Farag")

        exception_msg = excinfo.value.args[0]
        assert exception_msg == "Name must be a string"

    def test_first_name_failure(self):
        """ Make sure an invalid last name raises exceptions """

        # Last name is empty
        with pytest.raises(ValueError) as excinfo:
            _ = Person(3, first_name = "Farag")

        exception_msg = excinfo.value.args[0]
        assert exception_msg == "Last name was empty"

        # Last name is not string (int)
        with pytest.raises(TypeError) as excinfo:
            _ = Person(3,first_name = "Jason", last_name = 4.5)

        exception_msg = excinfo.value.args[0]
        assert exception_msg == "Last name must be a string"

        # First name is not string (List[int])
        with pytest.raises(TypeError) as excinfo:
            p1.last_name = [1,2]

        exception_msg = excinfo.value.args[0]
        assert exception_msg == "Last name must be a string"
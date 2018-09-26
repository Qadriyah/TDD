import unittest
from user import User
from validate_input import ValidateInput


class TestUserRegistration(unittest.TestCase):

    def setUp(self):
        #  New user
        self.new_user = {
            "name": "Sekitoleko Baker",
            "username": "Becks",
            "age": 30,
            "gender": "Male",
            "email": "becks@gmail.com",
            "password": "mUkungu$.001"
        }
        #  User
        self.user = User(self.new_user)
        #  ValidateInput
        self.user_input = ValidateInput(self.new_user)

    def test_user_object(self):
        """Tests if created object is an instance of User"""
        self.assertEquals(isinstance(self.user, User), True,
                          msg="Object should be of type User")

    def test_password(self):
        """
        Tests if password is not less than 4 characters, contains
        a capital letter, a small letter, a digit and a special
        character
        """
        is_less = self.user_input.is_password_contain_capital_letter()
        is_upper = self.user_input.is_password_contain_capital_letter()
        is_lower = self.user_input.is_password_contain_small_letter()
        is_digit = self.user_input.is_password_contain_digit()
        is_char = self.user_input.is_password_contain_special_char()
        is_greater = self.user_input.is_username_greater_than_four()
        self.assertNotIn(False,
                         [is_less, is_upper, is_lower,
                             is_digit, is_char, is_greater],
                         msg="Password should contain a capital letter, a small letter, a digit, a character and should be more than 4 characters")

    def test_username(self):
        """
        Tests if the username is not the same as name and username
        not less than 4 characters
        """
        is_name = self.user_input.is_username_same_as_name()
        is_greater = self.user_input.is_username_greater_than_four()
        self.assertNotIn(False,
                         [is_name, is_greater],
                         msg="Username should not be the same as name and should be greater than 4 characters")

    def test_email(self):
        """Tests if the email is in the format b@gmail.com"""
        is_email = self.user_input.validate_email()
        self.assertEqual(True, is_email, msg="Password should be in ")

    def test_age(self):
        """Tests if age is a number and not greater than 0"""
        age = self.user_input.validate_age()
        self.assertEqual(True, age,
                         msg="Age should be a number and greater than 0")

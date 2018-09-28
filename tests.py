import unittest
from unittest.mock import patch

from validate_input import ValidateInput
from user import User
from app import MainApp


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
        self.validator = ValidateInput(self.user)
        #  Users DB
        self.users = {self.user.password: self.user}
        #  main file
        self.app = MainApp()
        self.app.register_user(self.user, self.validator)
        self.app.login_user(self.user.email, self.user.password)

    def test_user_object(self):
        """Tests if created object is an instance of User"""
        self.assertEqual(isinstance(self.user, User), True,
                         msg="Object should be of type User")

    def test_password(self):
        """
        Tests if password is not less than 4 characters, contains
        a capital letter, a small letter, a digit and a special
        character
        """
        self.assertEqual(True, self.validator.validate_password(),
                         msg="Password should contain a capital letter, a small letter, a digit, a character and should be more than 4 characters")

    def test_username(self):
        """
        Tests if the username is not the same as name and username
        not less than 4 characters
        """
        self.assertEqual(True, self.validator.validate_username(),
                         msg="Username should not be the same as name and should be greater than 4 characters")

    def test_email(self):
        """Tests if the email is in the format b@gmail.com"""
        self.assertEqual(True, self.validator.validate_email(),
                         msg="Password should be in ")

    def test_age(self):
        """Tests if age is a number and not greater than 0"""
        self.assertEqual(True, self.validator.validate_age(),
                         msg="Age should be a number and greater than 0")

    def test_gender(self):
        """Tests if gender is either Male or Female"""
        self.assertEqual(True, self.validator.validate_gender(),
                         msg="Gender should either be Male or Female")

    def test_name(self):
        """Tests if name is empty"""
        self.assertEqual(True, self.validator.validate_name(),
                         msg="Name must not be empty")

    def test_register_user(self):
        """Tests if the user is registered successfully"""
        self.assertEqual(self.app.register_user(self.user, self.validator),
                         "User registered successfully")

    def test_login_user(self):
        """Tests if user login successfully"""
        self.app.register_user(self.user, self.validator)
        self.assertEqual(self.app.login_user(
            self.user.email, self.user.password), "Login successful")

    def test_logout(self):
        """Tests if user logs out successfully"""
        self.assertEqual(self.app.logout(), "You have logged out")

    def test_change_password(self):
        """Tests if password is chnaged successfully"""
        self.assertEqual(self.app.change_password(
            "mUkungu$.001", "Dick@22"), "Password has been changed successfully")

    def test_change_email(self):
        """Tests if email changes successfully"""
        self.assertEqual(self.app.change_email(
            "mUkungu$.001", "berkins@yahoo.com"), "Email changed successfully")

    def test_authenticate_user(self):
        """Tests if user exists"""
        self.app.register_user(self.user, self.validator)
        self.assertEqual(self.app.authenticate_user(
            "becks@gmail.com", "mUkungu$.001")[0], True)

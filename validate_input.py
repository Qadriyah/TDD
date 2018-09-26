import re


class ValidateInput:

    def __init__(self, input_data):
        self.input_data = input_data

    def is_password_greater_than_four(self):
        """
        Checks if the password length is not less than 4 charaters

        Returns:
            bool: True for success, False otherwise
        """
        if len(self.input_data["password"]) >= 4:
            return True
        return False

    def is_password_contain_small_letter(self):
        """
        Checks if the password cotains a small letter

        Returns:
            bool: True for success, False otherwise
        """
        if re.search(r"[a-z]", self.input_data["password"]):
            return True
        return False

    def is_password_contain_capital_letter(self):
        """
        Checks if the password cotains a capital letter

        Returns:
            bool: True for success, False otherwise
        """
        if re.search(r"[A-Z]", self.input_data["password"]):
            return True
        return False

    def is_password_contain_digit(self):
        """
        Checks if the password cotains a digit

        Returns:
            bool: True for success, False otherwise
        """
        if re.search(r"[0-9]", self.input_data["password"]):
            return True
        return False

    def is_password_contain_special_char(self):
        """
        Checks if the password cotains a special character

        Returns:
            bool: True for success, False otherwise
        """
        if re.search(r"[@!#$%^&*()_+=|?/\-~}{;:.<>,]",
                     self.input_data["password"]):
            return True
        return False

    def is_username_greater_than_four(self):
        """
        Checks if the username is greater or equal to four characters

        Returns:
            bool: True for success, False otherwise
        """
        if len(self.input_data["username"]) >= 4:
            return True
        return False

    def is_username_same_as_name(self):
        """
        Checks if the username is the same as the name

        Returns:
            bool: True for success, False otherwise
        """
        if self.input_data["username"] == self.input_data["name"]:
            return False
        return True

    def validate_email(self):
        """
        Checks if the email is in the format johndoe@gmail.com

        Returns:
            bool: True for success, False otherwise
        """
        if re.search(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)",
                     self.input_data["email"]):
            return True
        return False

    def validate_age(self):
        """
        Checks if age is a number and not less than 0

        Returns:
            bool: True for success, False otherwise
        """
        if isinstance(self.input_data["age"], int) and self.input_data["age"] > 0:
            return True
        return False

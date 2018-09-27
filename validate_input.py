import re


class ValidateInput:

    def __init__(self, input_data):
        self.input_data = input_data
        self.error = {}

    def validate_password(self):
        """
        Checks if the password length is not less than 4 charaters, 
        contains a digit, an uppercase letter, a lowercase letter 
        and a character

        Returns:
            bool: True for success, False otherwise
        """
        lowercase_letter = re.search(r"[a-z]", self.input_data.password)
        uppercase_letter = re.search(r"[A-Z]", self.input_data.password)
        contain_digit = re.search(r"[0-9]", self.input_data.password)
        special_char = re.search(
            r"[@!#$%^&*()_+=|?/\-~}{;:.<>,]", self.input_data.password)

        if len(self.input_data.password) < 4 or None in [lowercase_letter, uppercase_letter, contain_digit, special_char]:
            return False
        return True

    def validate_username(self):
        """
        Checks if the username is greater or equal to four characters
        and not the same as name

        Returns:
            bool: True for success, False otherwise
        """
        if len(self.input_data.username) < 4 or self.input_data.username == self.input_data.name:
            return False
        return True

    def validate_email(self):
        """
        Checks if the email is a valid email and it's in 
        the format johndoe@gmail.com

        Returns:
            bool: True for success, False otherwise
        """
        if re.search(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)",
                     self.input_data.email):
            return True
        return False

    def validate_age(self):
        """
        Checks if age is a number and not less than 0

        Returns:
            bool: True for success, False otherwise
        """
        if isinstance(self.input_data.age, int) and self.input_data.age > 0:
            return True
        return False

    def validate_gender(self):
        """
        Checks if gender is either Male or Female

        Returns:
            bool: True for success, False otherwise
        """
        if self.input_data.gender == "Male" or self.input_data.gender == "Female":
            return True
        return False

    def validate_name(self):
        """
        Checks if name is not blank

        Returns:
            bool: True for success, False otherwise
        """
        if not self.input_data.name:
            return False
        return True

from user import User
from validate_input import ValidateInput


class MainApp:
    users = {}

    def main(self):
        pass

    def register_user(self, user, validator):
        if not validator.validate_username():
            return "Username must not be the same as Name and must be more than 4 characters"

        if not validator.validate_name():
            return "Name must not be empty"

        if not validator.validate_age():
            return "Age must be a number and not less than 0"

        if not validator.validate_email():
            return "Wrong email address"

        if not validator.validate_gender():
            return "Gender should either be Male or Female"

        if not validator.validate_password():
            return "Password must be more than 4 characters, \
            contain an uppercase letter, a lowercase letter, \
            a number and a character"

        self.users.update({user.email: user})
        return "User registered successfully"

    def login_user(self, user):
        if not self.authenticate_user(user.email, user.password):
            return "User does not exist"
        return "Login successful"

    def authenticate_user(self, email, password):
        check = False
        for key in self.users.keys():
            if key == email:
                self.users[key].status = "Active"
                check = True
                break
        return check

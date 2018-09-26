from validate_input import ValidateInput


class User:

    def __init__(self, user):
        self.name = user["name"]
        self.username = user["username"]
        self.age = user["age"]
        self.password = user["password"]
        self.email = user["email"]
        self.gender = user["gender"]

    def register_user(self, user):
        pass

    def login_user(self, email, password):
        pass

    def change_email(self, user, new_email):
        pass

    def change_password(self, user, new_password):
        pass

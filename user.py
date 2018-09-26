class User:
    def __init__(self, user):
        self.name = user["name"]
        self.username = user["username"]
        self.age = user["age"]
        self.password = user["password"]
        self.email = user["email"]
        self.gender = user["gender"]
        self.status = "Inactive"

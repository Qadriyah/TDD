import time
from beautifultable import BeautifulTable

from user import User
from validate_input import ValidateInput


class MainApp:
    users = {}
    session = []

    def main(self):
        """
        The main function that handles protected routes
        """
        menu = {
            1: "Change your email",
            2: "Change your password",
            3: "Display registered users",
            4: "Register users",
            5: "Logout"
        }
        #  Display the menu for the protected routes
        for key, option in menu.items():
            print("{}. {}".format(key, option))

        selected_option = input("Select an option: ")
        try:
            selected_option = int(selected_option)
            #  Check if the selected option exists on the menu
            menu_options = list(menu.keys())
            if selected_option not in menu_options:
                print("[+] The selected item does not exists\n")
                return self.main()

            if selected_option == 1:
                print("CHANGE YOUR EMAIL")
                current_password = input("Enter your current password: ")
                new_email = input("Enter new email: ")
                print("[+] Changing email...")
                response = self.change_email(current_password, new_email)
                time.sleep(2)
                print("[+] {}\n".format(response))
                print("\nYou are logged in as {}\n".format(self.session[0]))
                return self.main()

            if selected_option == 2:
                print("CHANGE YOUR PASSWORD\n")
                old_password = input("Enter current password: ")
                new_password = input("Enter new password: ")
                response = self.change_password(old_password, new_password)
                print("[+] Changing password...")
                time.sleep(2)
                print("[+] Logging out...")
                time.sleep(2)
                print("[+] {}\n".format(response))
                return self.login()

            if selected_option == 3:
                table = BeautifulTable()
                table.column_headers = ["#",
                                        "Name",
                                        "Username",
                                        "Age",
                                        "Gender",
                                        "Email",
                                        "Status"]
                for index, user in enumerate(self.users.values()):
                    table.append_row([index+1,
                                      user.name,
                                      user.username,
                                      user.age,
                                      user.gender,
                                      user.email,
                                      user.status])
                table._column_alignments["Name"] = BeautifulTable.ALIGN_LEFT
                table._column_alignments["Username"] = BeautifulTable.ALIGN_LEFT
                table._column_alignments["Gender"] = BeautifulTable.ALIGN_LEFT
                table._column_alignments["Email"] = BeautifulTable.ALIGN_LEFT
                table._column_alignments["Status"] = BeautifulTable.ALIGN_LEFT
                print(table)
                self.main()

            if selected_option == 4:
                self.register()

            if selected_option == 5:
                response = self.logout()
                print("[+] Logging out...")
                time.sleep(2)
                print("[+] {}\n".format(response))
                return

        except ValueError:
            print("[+] Your option should be a number\n")
            return self.main()

    def register(self):
        """
        Gets user input and invokes the register_user that 
        handles the validations registers a new user

        Returns:
            function call: Call to itself
        """
        print("\nEnter your details to register\n")
        try:
            name = input("Name: ")
            username = input("Username: ")
            gender = input("Gender: ")
            age = int(input("Age: "))
            email = input("Email: ")
            password = input("Password: ")

            #  New user
            new_user = User({
                "name": name,
                "username": username,
                "age": age,
                "gender": gender,
                "email": email,
                "password": password
            })
            validator = ValidateInput(new_user)
            app = MainApp()
            response = app.register_user(new_user, validator)
            print("[+] Registering user...")
            time.sleep(2)
            if response == "User registered successfully":
                print("[+] {}\n".format(response))
                #  Check if user is already logged in
                if len(self.session) > 0:
                    return self.main()

                return self.login()
            print("[+] {}".format(response))
            return self.register()

        except ValueError:
            print("Only numbers are allowed for age\n")
            return self.register()

    def login(self):
        """
        Gets user login details and creates a session for the user
        """
        app = MainApp()
        print("Enter your email and password to LOGIN\n")
        email = input("Email: ")
        password = input("Password: ")
        response = app.login_user(email, password)
        print("[+] Logging in...")
        time.sleep(2)
        if response == "Login successful":
            print("\nYou are logged in as {}".format(self.session[0]))
            return self.main()

        print("[+] {}\n".format(response))
        return self.login()

    def register_user(self, user, validator):
        """
        Registration helper method that makes all the input 
        validations

        Args:
            user(object): A User object
            validator(object): A ValidateInput object

        Returns:
            str: A success message
        """
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
            return "Password must be more than 4 characters, contain an uppercase letter, a lowercase letter, a number and a character"

        self.users.update({user.email: user})
        return "User registered successfully"

    def login_user(self, email, password):
        """
        Creates a session for the successfully logged in user

        Agrs:
            email(str): Email used during registration
            password(str): Password created at registration

        Returns:
            str: Describes if the operation was a success or failure
        """
        is_auth = self.authenticate_user(email, password)
        if not is_auth[0]:
            return "User does not exist"
        self.session.append(is_auth[1])
        return "Login successful"

    def authenticate_user(self, email, password):
        """
        Checks if user exists and sets the status to Active 
        that indicates a logged in user

        Agrs:
            email(str): Email used during registration
            password(str): Password created at registration

        Returns:
            tuple: With two elements, a bool and the user's email
        """
        check = False
        for key in self.users.keys():
            if key == email:
                self.users[key].status = "Active"
                check = True
                break
        return check, email

    def logout(self):
        """
        Destroys the login session

        Returns:
            str: Message describing a successful operation
        """
        self.users[self.session[0]].status = "Inactive"
        self.session.clear()
        return "You have logged out"

    def change_password(self, old_password, new_password):
        """
        Changes the user's password and redirects them back to the
        login window

        Args:
            old_password(str): The current user's password
            new_password(str): The new password

        Returns:
            str: Message that describes if the operation was 
            a success or failure
        """
        user = self.users[self.session[0]]
        if user.password == old_password:
            self.users[self.session[0]].password = new_password
            self.logout()
            return "Password has been changed successfully"
        return "Wrong old password"

    def change_email(self, password, new_email):
        """
        Changes the email of the user and updates the session

        Args:
            password(str): The current user's password 
            new_email(str): The new user's email
        """
        user = self.users[self.session[0]]
        if user.password == password:
            self.users[new_email] = self.users.pop(self.session[0])
            self.users[new_email].email = new_email
            self.session.clear()
            self.session.append(new_email)
            return "Email changed successfully"
        return "Wrong password"


if __name__ == "__main__":
    print(":::::::::::::::: WELCOME TO TDD :::::::::::::::\n")
    app = MainApp()
    app.register()

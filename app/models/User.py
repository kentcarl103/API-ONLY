class User:
    def __init__(self, firstname, lastname, email, password, position, middlename=""):
        self.firstname = firstname
        self.middlename = middlename  # optional
        self.lastname = lastname
        self.email = email
        self.password = password
        self.position = position

    def to_dict(self):
        return {
            "firstname": self.firstname,
            "middlename": self.middlename,
            "lastname": self.lastname,
            "email": self.email,
            "password": self.password,
            "position": self.position
        }

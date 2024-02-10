#!/usr/bin/python3
"""define class"""


class User(BaseModel):
    num = 0
    def __init__(self, email="", password="",first_name="",last_name=""):
        """constructor"""
        super().__init__(name=email, age=password)
        self.email = email
        self.password = password
        self.first_name = first_name
        self.last_name = last_name

        User.num += 1

    def display_user(self):
        print(f"{self.email}, {self.password}, {self.first_name}, {self.last_name}")
print(f"{User.num}")

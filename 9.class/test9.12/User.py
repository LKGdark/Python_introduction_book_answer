class User:
    def __init__(self,first_name,last_name,age,sex):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.sex = sex
    
    def describe_user(self):
        print(f"{self.first_name.title()} {self.last_name.title()} is a {self.sex.lower()},and age is {self.age}")

    def greet_user(self):
        print(f"Hello ! {self.first_name.title()} {self.last_name.title()}")

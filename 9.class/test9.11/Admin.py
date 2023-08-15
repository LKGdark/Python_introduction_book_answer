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


class Privileges():
    def __init__(self,*privileges):
        self.privileges_list = []
        for privilege in privileges:
            self.privileges_list.append(privilege)
    def show_privileges(self):
        for privilege in self.privileges_list:
            print(privilege)


class Admin(User):
    def __init__(self,first_name,last_name,age,sex,*privileges):
        super().__init__(first_name,last_name,age,sex)
        self.privileges = Privileges(*privileges)


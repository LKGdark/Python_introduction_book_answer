from User import User
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


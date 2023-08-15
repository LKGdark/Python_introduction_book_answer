class User:
    def __init__(self,first_name,last_name,age,sex):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.sex = sex
        self.login_attemps = 0
    
    def describe_user(self):
        print(f"{self.first_name.title()} {self.last_name.title()} is a {self.sex.lower()},and age is {self.age}")

    def greet_user(self):
        print(f"Hello ! {self.first_name.title()} {self.last_name.title()}")
    
    def increment_number_attemps(self):
        """将login_attemps的数值加1"""
        print("login attemps +1")
        self.login_attemps += 1

    def reset_number_attemps(self):
        """将login_attemps的数值清0"""
        print("login attemps = 0")
        self.login_attemps = 0
    

Cai_Xukun = User('cai','xukun','22','woman')
Cai_Xukun.increment_number_attemps()
Cai_Xukun.increment_number_attemps()
Cai_Xukun.increment_number_attemps()
print(Cai_Xukun.login_attemps)
Cai_Xukun.reset_number_attemps()
print(Cai_Xukun.login_attemps)
from pathlib import Path
import json

def bulid_user(**user_info):
    user_info['name'] = input("Input name:")
    user_info['age'] = int(input("Input age:"))
    user_info['sex'] = input("Input sex:")
    return user_info

def user_name_right(path):
    name = input("What is your name:")
    contents = path.read_text()
    front_user = json.loads(contents)
    if front_user ['name'] == name:
        return True
    else:
        return False
    
def user_data_write(path):
    u_data = bulid_user()
    contents = json.dumps(u_data)
    path.write_text(contents)

def user_data_read(path):
    contents = path.read_text()
    u_data = json.loads(contents)
    print(f"user data:\n        {u_data}")

def greet_user():
    path = Path(input("Please input your file name:"))
    if path.exists() :
        if user_name_right(path):
            user_data_read(path)
        else:
            user_data_write(path)
    else:
        user_data_write(path)
        

greet_user()
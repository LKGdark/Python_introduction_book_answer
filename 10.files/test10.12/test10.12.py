from pathlib import Path
import json

def favourite_num_write():
    """输入你喜欢的数字，我会将它转变为json文件并保存至favourite_number.json"""
    favourite_number = input("Input your favourite number:")
    path = Path('favourite_num.json')
    contents = json.dumps(favourite_number)
    path.write_text(contents)

def favourite_num_read():
    """读取你最喜欢的数字"""
    path = Path('favourite_num.json')
    if path.exists():
        favourite_number = path.read_text()
        contents = json.loads(favourite_number)
        print(f"Your favouerite number is {favourite_number}")
    else:
        favourite_num_write()

favourite_num_read()
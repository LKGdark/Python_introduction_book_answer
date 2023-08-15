from pathlib import Path

user_input = input("Please input your name,and I will put your name in 'guest.txt':")
path = Path('guest.txt')
path.write_text(user_input)
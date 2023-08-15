from pathlib import Path

path = Path('guest_book.txt')

print('按q退出程序')
user_input = ''
contents = ''
while True:
    user_input = input('Input your name:')
    if user_input == 'q':
        break

    contents += (user_input+'\n')

path.write_text(contents)
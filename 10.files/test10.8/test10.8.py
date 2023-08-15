from pathlib import Path
# path = Path('cat.txt111')
# try:
#     contents = path.read_text()
# except FileNotFoundError:
#     print("文件不存在")
# else:
#     print(contents)

path = Path('cat.txt')
try:
    contents = path.read_text()
except FileNotFoundError:
    print("文件不存在")
else:
    print(contents)
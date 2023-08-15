from pathlib import Path
path = Path('dog.txt')
try:
    contents = path.read_text()
except FileNotFoundError:
    pass
else:
    print(contents)

path = Path('test10.8/cat.txt')
try:
    contents = path.read_text()
except FileNotFoundError:
    pass
else:
    print(contents)
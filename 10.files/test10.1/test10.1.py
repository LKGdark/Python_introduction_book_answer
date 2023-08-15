from pathlib import Path

path = Path('learning_python.txt')
contents = path.read_text().rstrip()
print(contents)


for line in contents.splitlines():
    print(line)
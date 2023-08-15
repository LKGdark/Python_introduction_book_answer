from pathlib import Path

path = Path('test10.1/learning_python.txt')
contents = path.read_text().rstrip()


for line in contents.splitlines():
    print(line)

for line in contents.splitlines():
    line1 = line.replace('Python','C')
    print(line1)

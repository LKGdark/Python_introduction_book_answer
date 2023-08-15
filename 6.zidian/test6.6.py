favourite_langues = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python',
    }

names = ['jen','sarah','bob','kidw']

for name in names:
    if name in favourite_langues.keys():
        print(f"Thanks for {name}'s invited search!")
    elif name not in favourite_langues.keys():
        print(f"I want to invite {name},could you join?")
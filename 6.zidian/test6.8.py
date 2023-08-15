dog = {
    'type': 'middle',
    'admin': 'dsasda',
    }

cat = {
    'type': 'middle',
    'admin': 'fsdfa',
    }

rabbit = {
    'type': 'little',
    'admin': 'gfdfvfs',
    }

pets = [dog, cat, rabbit]
for pet in pets:
    print(f"This pet type is {pet['type']}")
    print(f"This pet admin is {pet['admin']}\n")
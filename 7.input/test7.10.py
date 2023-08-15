responses = {}
polling_active = True

while polling_active :
    name = input("\nWhat is your name?")
    response = input ("If you could visit one place in the world,where would you go?")

    responses[name] = response

    repeat = input ("Would you like to add somebody?")
    if repeat.upper() == 'NO':
        polling_active = False

print("\n-----Result : -----\n")
for name,response in responses.items() :
    print(f"{name} would like to go to {response}!")
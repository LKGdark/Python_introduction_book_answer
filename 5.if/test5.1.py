car="BMW"
print("Is car == 'bmw'?I predict True.")
print(car.lower()=='bmw')

print("\nIs car == 'audi'?I predict False.")
print(car.lower()=='audi')

animals=['dog','cat','duck','bird','snack','mouse']
animal='dog'
print("\nIs animal in animals?I predict True")
if animal in animals:
    print(animal in animals)
else:
    print(animal not in animals)

animals=['dog','cat','duck','bird','snack','mouse']
print("\nIs wolf in animals?I predict False")
print('wolf' in animals)

foods=('apple','pizza','banana','rice','pear','noodles')
if 'shit' in foods:
    print("shit in foods\n")
else :
    print("shit not in foods\n")

age = 18
if(age >20):
    print("age>20")
else :
    print("age<=20\n")

age1=30
age2=35

if(age1>age and age2>age):
    print("age1 and age2 >age is True\n")
else :
    print("age and age2 > age is False\n")

if(age1<age or age2<=age):
    print("age1 or age2 <= age is True\n")
else :
    print("age or age2 <= age is False\n")

age=33

print("age=33")
if(age1<age or age2<=age):
    print("age1 or age2 <= age is True\n")
else :
    print("age1 or age2 <= age is False\n")
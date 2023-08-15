age = input("How old are you ? \n")
age = int(age)
if age >= 200 :
    print("Age error!\n")
elif age >= 12 :
    print("Please charge 15$\n")
elif age >= 3 :
    print("Please charge 10$\n")
elif age >= 0 :
    print("Free of you \n")
else :
    print("Age error!\n")
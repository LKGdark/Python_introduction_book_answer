str1="That is a test string"
str2="This is a test string"
if str1==str2:
    print("str1==str2\n")
else :
    print("str1!=str2\n")

print("str1=str2")
str1=str2
if str1==str2:
    print("str1==str2\n")
else :
    print("str1!=str2\n")

animal1='Cat'
if (animal1.lower()=='cat'):
    print("animal1=='cat'\n")

animal2='Dog'
if (animal2.lower()!='cat'):
    print("animal2 !='cat'\n")

num1=77
num2=33
print("Is num1 > num2 ?")
print(num1>num2)

print("\nIs num1 <= num2 ?")
print(num1<=num2)

print("\nIs num1 == num2 ?")
print(num1 == num2)

print("\nIs num1 != num2 ?")
print(num1 != num2)

nums=range(1,13,3)
if 3 in nums:
    print("3 in nums")
else :
    print("3 not in nums")

if 4 in nums:
    print("4 in nums")
else :
    print("4 not in nums")

if 4 in nums and 7 in nums:
    print("4 and 7 in nums")
else :
    print("4 and 7 not in nums")
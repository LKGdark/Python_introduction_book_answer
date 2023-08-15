from random import choice

caipiao = [1,2,3,4,5,6,7,8,9,10,'a','b','c','d','e']
choice_all = []
num = 0
for i in range(4):
    choice_all.append(choice(caipiao))

print(f"If you find {choice_all},you can win lots of money")
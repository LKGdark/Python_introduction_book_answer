from random import choice

caipiao = [1,2,3,4,5,6,7,8,9,10,'a','b','c','d','e']

def ticket_num():
    choice_all = []
    num = 0
    for i in range(4):
        choice_all.append(choice(caipiao))
    return choice_all

choice_ben = ticket_num()

print(f"If you find {choice_ben},you can win lots of money")

my_ticket = []
sum = 0
while my_ticket != choice_ben :
    my_ticket = ticket_num()
    print(f"my ticket is {my_ticket}")
    sum += 1

if my_ticket == choice_ben:
    print(f"congratulations！you win 100_000_000 ￥,you buy {sum} ticket")

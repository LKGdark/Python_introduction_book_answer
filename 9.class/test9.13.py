from random import randint

class Die:
    def __init__(self,sides=6):
        self.sides = sides
    
    def roll_die(self,num):
        number = 0
        while number != num :
            number += 1
            n = randint(1,self.sides)
            print(f"This Die sides is {n}")
        print("---------------------------")
    
die6 = Die(6)
die6.roll_die(10)

die10 = Die(10)
die10.roll_die(10)
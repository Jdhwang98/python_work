# 2024-07-12 13:31:51
from random import randint
class Die:
    def __init__(self, sides=6):
        self.sides = sides
        
    def roll_die(self):
        return randint(1,self.sides)
   

die6 = Die()
rolls = []
for num_of_rolls in range(10):
    roll = die6.roll_die()
    rolls.append(roll)
print(rolls)
    

d10 = Die(10)
rolls = []
for num_rolls in range(10):
    roll = d10.roll_die()
    rolls.append(roll)
print(rolls)

d20 = Die(20)
rolls = []
for num_rolls in range(10):
    roll = d20.roll_die()
    rolls.append(roll)
print(rolls)
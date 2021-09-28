import random
mind = random.randint(1,9)
chances = 0
print("guess the number between 1-9")
while chances<5 :
    number=int(input("enter your guess  "))
    if number==mind :
        print("your guess is correct")
        break
    elif number<mind :
        print("think of a higher number")
    else :
        print("think of a smaller number")
    chances = chances+1
if chances>4 :
    print("you lose the number is ",mind)
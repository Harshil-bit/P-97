import random
num= random.randint(1,9)
print("Number Guessing game")
print("Guess a number (between 1 and 9)")
chances=0
while chances<5:
    guess= int(input("Enter your guess:- "))  
    if(num==guess):
        print("Congralutation, YOU WON!!!")
        break
    elif guess<num:
        print("Your number is too low. Guess a higher number than ",num)
    else:
        print("Your number is too high. Guess a lower number than ",num)
    chances+=1
if not chances<5:
    print("You lose the game. The number is ",num)
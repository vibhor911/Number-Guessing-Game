
import random
print("Number Guessing Game")
number = random.randint(1,9)

print("Guess a number (between 1 and 9):")

while chances < 5:

   guess=int(input("Enter your guess:- "))

   if guess == number:
    print("Congraulation you won!!!")
   break

elif guess <=number:
     print("your guess was too low: Guess a number higer than",guess)
 
    else:
       print("your guess was too high: Guess a number lower than",guess)
        chances += 1

        if not chances < 5:
             print("YOU LOSE!! The number is",number)
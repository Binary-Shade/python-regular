import random

x=random.randint(1,100)
print("|-----------------------|")
print("| number guessing game  |")
print("|-----------------------|")
print("you have 7 tries to guess the number")
tries=1

while tries < 7:
    user_input=int(input("enter the number ?"))
    if user_input == x:
        print("you found the number in "+ str(tries) +" try")
        break
    elif user_input < x:
        print("your guess is small")
    else:
        print("your guess to large")
    tries+=1
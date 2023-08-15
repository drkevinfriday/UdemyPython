import random
highest = 10
guess = 0 # initialize the while loop
answer = random.randint(1,highest)

print("Please guess number between 1 and {}: ".format(highest))


while guess != answer:
    guess = int(input())
    if guess == answer:
        print(" You've guessed he correct number")
    else:
        if guess <  answer:
            print("Please guess higher")
        else:
            print("Please guess lower")
        
        # if guess == answer:
        #     print("great job you got it!")
        # else: 
        #     print("Sorry you guessed wrong")




    

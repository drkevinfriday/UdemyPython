from pickle import TRUE


low = 1 
high = 10

print("Please think of a number  between {} and {} ".format(low,high))
input("Please press enter")

guess_count = 1 

while low != high:
    guess = low + (high -low) // 2
    high_low = input("My guess is {}. Should i guess higher or lower?  Enter h or l or c if my guess was correct".format(guess).casefold())

    if high_low == "h":
        pass
        low = guess + 1
        # guess higher
    elif high_low == "l":
        pass
        # guess lower
        high = guess - 1
    if high_low == "c":
        pass
        print("You got it correct the answer is {}".format(guess))
        break
    else:
        print("Please enter h, l or c")

    guess_count = guess_count + 1
else:
    print("the answer is {} we got it in {} guesses".format(high_low, guess_count
    ))
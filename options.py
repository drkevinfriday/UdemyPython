#list of options
options = ["Learn Python", "Learn Java", "Go swimming", "Have dinner", "Go to bed", "Exit"]
while True:    
    
    print("test")
    print("Please choose your option from the list below: ")
# produces the list  of options from the list
    for option in options:
        print("{}:\t{}\n".format(options.index(option),option))
# Get the selection input from the user
    selection = (input("Enter your selection here:  "))
 
# this example shows how to write the code using the (in) operator
    if selection == "5":
        break
    elif selection in "01234":
        print("You choose to {}".format(options[int(selection)]))

    else:
        print("You entered the wrong selection")
        print("Please enter 1, 2, 3, 4, or 5")


# this example shows how to write the code using the (if) operator
    # if selection == 0:
    #     pass
    #     print("You choose to {}".format(options[0]))
        
    # elif selection == 1:
    #     pass
    #     print("You choose to {}".format(options[1]))
    # elif selection == 2:
    #     pass
    #     print("You choose to {}".format(options[2]))
    # elif selection == 3:
    #     pass
    #     print("You choose to {}".format(options[3]))
    # elif selection == 4:
    #     pass
    #     print("You choose to {}".format(options[4]))
    # elif selection == 5:
    #     pass
    #     print("You choose to {}".format(options[5]))
    #     break
    # else:
    #     print("You entered the wrong selection")
    #     print("Please enter 1, 2, 3, 4, or 5")






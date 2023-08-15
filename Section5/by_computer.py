selection = "-"
computer_parts = []
valid_choices = []
# parts_list = ["computer", "monitor","keyboard","mouse", "mouse mat"]

# while True:
#     for part in parts_list:
#         print("{}:\t{}\n".format(parts_list.index(part),part))

#                 # Get the selection input from the user
#         current_choice = (input("Enter your selection here:  "))



#list of options
options = [ "monitor","keyboard","mouse", "mouse mat","computer", "hdmi","to finish"]

#get the length of the list to compare with uer input to validate choices
for i in range(1, len(options)+1):
    valid_choices.append(str(i))

while selection != "7":    


    print("Please choose your option from the list below: ")
# produces the list  of options from the list
    for number,option in enumerate(options):
        print("{}:\t{}\n".format(number + 1,option))
# Get the selection input from the user
    selection = (input("Enter your selection here:  "))

# this example shows how to write the code using the (in) operator
    if selection == "7":
        print("This is a list of the computer_parts you chosen: " )
        print(computer_parts)
        break
    if selection in valid_choices:
        print("You choose to {}. We are adding it to your list".format(options[int(selection)-1]))
        computer_parts.append(options[int(selection) - 1])


else:
    print("This is a list of the computer_parts you chosen: " )
    print(computer_parts)
       

    # if current_choice in "12345":
    #     print("adding {}".format(current_choice))
    #     if current_choice == "":
    #         computer_parts.append("")
    #     elif current_choice == "":
    #         computer_parts.append("")
    #     if current_choice == "":
    #         computer_parts.append("")
    #     if current_choice == "":
    #         computer_parts.append("")
    #     if current_choice == "":
    #         computer_parts.append("")
    # else:
        

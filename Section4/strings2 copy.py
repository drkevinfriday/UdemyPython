parrot = "Norwegian Blue"

# print(parrot)

# print(parrot[3])
# print(parrot[4])
# print()
# print(parrot[3])
# print(parrot[6])
# print(parrot[8])


# print(parrot[0:6:2])
# print(parrot[0:6:3])

number = input("Please enter a series of numbers using any separators you like: ")
separators = ""
for char in number:
    if not char.isnumeric():
        separators = separators + char
print(separators)

values = "".join(char if char  not in  separators else " " for char in number).split()
print(sum([int(val) for val in values]))



print(type(values))



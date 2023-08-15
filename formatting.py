#right aligned by default 
for i in range(1,13):
    print("No. {0:2} squared is  {1:4} and cubed is {2:4}".format(i, i**2, i**3))
print()
#left aligned
for i in range(1,13):
    print("No. {0:<2} squared is  {1:<4} and cubed is {2:<4}".format(i, i**2, i**3))
print()
#center aligned
for i in range(1,13):
    print("No. {0:^4} squared is  {1:^4} and cubed is {2:^4}".format(i, i**2, i**3))
print()
#center aligned
for i in range(1,13):
    print("No. {0:^4} squared is  {1:^4} and cubed is {2:^4}".format(i, i**2, i**3))

print()
print("Pi is approximately {0:12}".format(22/7))
print("Pi is approximately {0:12f}".format(22/7)) # with f it defaults 6 digit after the decimal
print("Pi is approximately {0:12.50f}".format(22/7)) # with 50f it  50 digit after the decimal
print("Pi is approximately {0:52.50f}".format(22/7))
print("Pi is approximately {0:62.50f}".format(22/7))
print("Pi is approximately {0:<72.50f}".format(22/7))
print("Pi is approximately {0:<72.60f}".format(22/7))





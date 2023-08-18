welcome = "welcome to my nightmare ", "Alice Cooper", 1975
bad = "Bad Company", "Bad company", 1974
budgie = "Nightflight", "Budgie", 1981
imelda = "More Mayhem", "Emilda May ", 2011
Metallica = "Ride the lighting", "Metallica", 1984 

# print(Metallica)
# print(Metallica[0])
# print(Metallica[1])
# print(Metallica[2])

# Metallica2 = list(Metallica)
# print(Metallica2)

# Metallica2[0] = "Master of Puppets" # type: ignore

title, artist, year = Metallica
print(title)
print(artist)
print(year)

table = ("Coffee table", 200, 100, 75, 34.50)
print(table[1] * table[2])

name, length, width, height, price = table
print("The are of the table is {}".format(length * width))
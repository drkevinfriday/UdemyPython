pangram = "the quick brown  fox jumps over the lazy dog "
words = pangram.split()
print(words)


numbers= "9,233,372,036,854,775,807"
print(numbers.split(","))
print()
num = (numbers.split(","))

for index, value in enumerate(num):
    print(index, value)
    num[index]= int(value) # type: ignore
    




print(num)
print(type(num[0]))




# # values= "".join(generated_list)
# print(values)


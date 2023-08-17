pangram = "the quick brown  fox jumps over the lazy dog "

letters = sorted(pangram)
letters.remove(",")
print(letters)
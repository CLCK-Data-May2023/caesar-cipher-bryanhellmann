# add your code here
user_phrase = input("Please enter a sentence: ")
user_phrase = user_phrase.lower()
new_phrase = ''
reg_alp = ["a", "b", "c", "d", "e", "f", "g", "h",
           "i", "j", "k", "l", "m", "n", "o", "p",
           "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
shifted_alp = ["f", "g", "h", "i", "j", "k", "l", "m",
               "n", "o", "p", "q", "r", "s", "t", "u",
               "v", "w", "x", "y", "z", "a", "b", "c", "d", "e"]
for letter in user_phrase:
    if letter in reg_alp:
        new_phrase += shifted_alp[reg_alp.index(letter)]
    else:
        new_phrase += letter
print("The encrypted sentence is:", new_phrase)
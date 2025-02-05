#
# I am  using this file to test string inputs
#
#

# word = input("Enter a word: ")
# # print("This is your word: ", word)

# for letter in word:
#     if letter.isupper():
#         print(letter, " is capitalized")

# Check for a palindrome
def palindrome_word(teststr):
    temp = teststr.lower()

    newstr = ""
    for c in temp:
        if c.isalnum():
            newstr += c
    
    reversestr = ""
    strindx = len(newstr)-1
    while (strindx >= 0):
        reversestr += newstr[strindx]
        strindx -= 1

    if newstr == reversestr:
        return True
    return


total = 0
test_words = []

for word in test_words:
    total += Answer.is_palindrome(word)
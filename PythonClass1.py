intro = input("please give your introduction: ")
characterCount = 0
wordCount = 1
for i in intro:
    characterCount = characterCount + 1
    if i == ' ' :
        wordCount = wordCount + 1

print ("number of characters used: ", characterCount)
print ("number of words used: ", wordCount)
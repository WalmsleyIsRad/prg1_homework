sentence = input("enter a sentence")
words = sentence.split(" ")
wordCount = {}       #this is dictionary

for word in words:
    if (word in wordCount):
        wordCount[word] += 1
    else:
        wordCount[word] = 1
print(wordCount)
#problem 1 
print("Please enter in a whole number")
number = int(input(""))
max = number
factors = []
for x in range(1,(max+1)):
    if(number%x == 0):
        factors.append(x)

lfactors = len(factors)

snumber = str(number)
llfactors = str(lfactors)
ffactors = str(factors)

print(snumber + " " + "has" + " " + llfactors + " " + "factors, which are " + ffactors)
  

#problem 2
print("Please enter in a word")
phonetic = []
word = str(input(""))
wordslist = word.split(" ")
for letters in word:
    if(str(letters) == "a"):
        phonetic.append("Alpha")
    elif(str(letters) == "b"):
        phonetic.append("Bravo")
    elif(str(letters) == "c"):
        phonetic.append("Charlie")
    elif(str(letters) == "d"):
        phonetic.append("Delta")
    elif(str(letters) == "e"):
        phonetic.append("Echo")
    elif(str(letters) == "f"):
        phonetic.append("Foxtrot")
    elif(str(letters) == "g"):
        phonetic.append("Golf")
    elif(str(letters) == "h"):
        phonetic.append("Hotel")
    elif(str(letters) == "i"):
        phonetic.append("Indigo")
    elif(str(letters) == "j"):
        phonetic.append("Juliet")
    elif(str(letters) == "k"):
        phonetic.append("Kilo")
    elif(str(letters) == "l"):
        phonetic.append("Lima")
    elif(str(letters) == "m"):
        phonetic.append("Mike")
    elif(str(letters) == "n"):
        phonetic.append("November")
    elif(str(letters) == "o"):
        phonetic.append("Oscar")
    elif(str(letters) == "p"):
        phonetic.append("Papa")
    elif(str(letters) == "q"):
        phonetic.append("Quebec")
    elif(str(letters) == "r"):
        phonetic.append("Romeo")
    elif(str(letters) == "s"):
        phonetic.append("Sierra")
    elif(str(letters) == "t"):
        phonetic.append("Tango")
    elif(str(letters) == "u"):
        phonetic.append("Uniform")
    elif(str(letters) == "v"):
        phonetic.append("Victor")
    elif(str(letters) == "w"):
        phonetic.append("Whiskey")
    elif(str(letters) == "x"):
        phonetic.append("X-Ray")
    elif(str(letters) == "y"):
        phonetic.append("Yankee")
    elif(str(letters) == "z"):
        phonetic.append("Zulu")
print(phonetic)

def decode_ellen_speak(letters):
    if(len(letters) == 1):
        return letters[0]
    elif(letters[0] == letters[1]):
        return letters[0] + decode_ellen_speak(letters[1:])
    else:
        return decode_ellen_speak(letters[1:])

print("Please enter in a sound a whale would make so this machine can translate")
word = input(">")
decode_ellen_speak(word)
def decode_ellen_speak(letters):
    count = 0
    letter_list = []
    separation_of_letters = letter_list.split(" ")
    original_value = separation_of_letters[count]
    current_value = separation_of_letters[count+1]
    if (str(original_value) == str(current_value)):
        return separation_of_letters.remove(current_value)
        count +=1
        decode_ellen_speak(letters)
    else:
        return decode_ellen_speak(letters)
        count += 1

print("Please enter in a sound a whale would make so this machine can translate")
word = input(">")
decode_ellen_speak(word)
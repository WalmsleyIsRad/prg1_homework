nicknames = {
    "Shawn": "Snuggle Whiff",
    "Radcliffe": "Rad C"
}

nicknames["Eric"] = "Whookiee"
nicknames["Tom"] = "Cowabunga"
nicknames["Doug"] = "Dawg"
print(nicknames)

answers = []

for values in nicknames:
    nn = nicknames[values]
    answer = (values + " goes by the name of " + str(nn))
    answers.append(answer)
print(str(answers))

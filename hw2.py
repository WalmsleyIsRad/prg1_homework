#Program #1

campers = int(input("campers"))

if (campers <=0):
    print ("Which dimensions have you entered")
elif (campers == 1):
    print ("Just you then?")
elif (campers == 2):
    print ("Bring marshmellows")
elif (campers >= 3 and campers <= 6):
    print ("More than 3 is a party")
elif (campers >= 7):
    print ("PARTY")

#Problem #2

print ("You are driving and the police stop you")

sl = int(input("speed limit"))
ys = int(input("your speed"))
bd = str(input("Is it your birthday?"))
ysbd = ys - 5
if(bd == "Yes" or "yes"):
    print("The officer sings happy birthday to you")
    if(ysbd <= sl):
        print("No ticket")
    elif(ysbd < (sl + 5)):
        print("Warning")
    elif(ysbd >= (sl + 5) and   ysbd < (sl + 15)):
        print("Small Ticket")
    elif(ysbd >= (sl + 15)):
        print("Big Ticket")
        if(ysbd == (sl * 2)):
            print("You lost your license")
else:
            if (ys <= sl):
                print("No ticket")
            elif(ys < (sl + 5)):
                print("Warning")
            elif(ys >= (sl + 5) and   ys < (sl + 15)):
                print("Small Ticket")
            elif(ys >= (sl + 15)):
                print("Big Ticket")
                if(ys == (sl * 2)):
                    print("You lost your license")

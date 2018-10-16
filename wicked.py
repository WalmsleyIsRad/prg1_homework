
print("Please enter in 5 numbers, separated by a space")
numbers = input("")      #input allows you to input ANYTHING you want
numbers_added = numbers.split(" ")      #split allows you to split them
if(len(numbers_added)==5):      #len asks for the length of numbers
    sum = 0
    for sx in numbers_added:     #turns list into floating points
        x = float(sx)
        sum +=x
    print(sum, "this is not your final score")
    
    score = 0
    for swicked in numbers_added:
        wicked = float(swicked)
        if(wicked == 13.0):
            score += -100
        elif(wicked == 7.0):
            score += 30
        elif(wicked %2 == 1):
            score += wicked*2
        elif(wicked %2 == 0):
            score += wicked/2
        else:
            print("not valid")
    print(score, " is your final score")
else:
    print("You did not enter in the numbers correctly")
    



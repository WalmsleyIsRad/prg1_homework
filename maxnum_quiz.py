print("Please enter in integers separated by a space")
numbers = input(">")
lnumbers = numbers.split(" ")
print(lnumbers)
for x in lnumbers:
    current_val = x
    stored_val = int(lnumbers)
    if current_val > stored_val:
        print("Your largest number is " + str(current_val))
    
    





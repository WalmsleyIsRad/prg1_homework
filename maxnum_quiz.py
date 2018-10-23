print("Please enter in integers separated by a space")
numbers = input(">")
number_list = numbers.split(" ")
max_number = int(number_list[0])
for number in number_list:
    inumber = int(number)
    if (max_number < inumber):
            max_number = inumber
print("the largest number is " + str(max_number))





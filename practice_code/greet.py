'''
def message(recipient,sender):
    print("Hello, "+recipient+ " How are you? What is up?")
    print("-"+sender)

student = "Patrick Walmsley"
teacher = "Mr. Gold"

message(student,teacher)

'''

#write a function that will tell you if a number is in the range of two other numbers

def number_in_range(low,high,number):
    if(low < number and high > number):
        return True
    else:
        return False

number1 = 1
number10 = 10
number_in_the_range = 4
number_out_range = -5
number_too_high = 100

print(number_in_range(number1,number10,number_in_the_range))
print(number_in_range(number1,number10,number_out_range))

#problem1

def swap(a,b):
    temp = a
    a = b
    b = temp
    return a,b
'''
x = 4
y = 17
answer = swap(x,y)
print(answer)
'''
#problem2
def bubble(items):
    item_found = False
    index = 0
    while not item_found and (index < len(items)):
        if(items[index-1] > 0 and items[index-1] > items[index]):
            swap(items[index-1],items[index])
            return True 
        else:
            return item_found
        index +=1
answer1 = [3,5,8,7,6]
answer2 = bubble(answer1)
print(answer2)

#problem3
def bubble_sort(items):
    count = 0
    while(count < len(items)):
        if(items[count-1] > 0 and items[count-1] > items[count]):
            bubble(items[count-1],items[count])
answer1 = bubble_sort(answer2)
print(answer2)









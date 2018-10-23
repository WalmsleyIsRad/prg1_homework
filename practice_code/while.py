print("How many times would you like to count")
count = int(input(">"))

y = 0
while(y < count):
    stars = ""
    x = 0
    while(x < count):
        x = x + 1
        stars += "*"
    print(stars)
    y += 1
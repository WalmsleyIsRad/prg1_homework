def merge(items):
    half = int(len(items)/2)
    items_left = items[:half]
    items_right = items[half:]
    if(len(items) == 1):
        return items
    elif(len(items_left) > 1):
        merge(items_left)
    elif(len(items_right) > 1):
        merge(items_right)

merge = [4,2,1,6,3,2,5]

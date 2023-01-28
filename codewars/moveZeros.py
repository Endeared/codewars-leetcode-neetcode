# kata 5

def move_zeros(lst):

    newList = []
    count = 0
    x = 0

    for num in lst:
        if num != 0:
            newList.append(num)
        elif num == 0:
            count += 1
    
    while x < count:
        newList.append(0)
        x += 1
    
    return newList
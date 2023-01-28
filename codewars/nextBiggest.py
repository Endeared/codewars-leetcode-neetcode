# kata 4 (my first!)

def next_bigger(n):
    check = list(str(n))
    original = []
    listSorted = []
    newNum = ""
    
    
    for digit in check:
        original.append(digit)
        
    listSorted = original.copy()
    print(listSorted)
    listSorted.sort(reverse=True)
    print(listSorted)
    print(original)
    
    if listSorted == original:
        return -1
    else:
        for num in listSorted:
            newNum += str(num)
        
    i = n
    newNum = int(newNum)
    
    for j in range(i + 1, newNum):
        toCheck = list(str(j))
        toCheck.sort()
        check.sort()
        if toCheck == check:
            return j
    
    return newNum
        
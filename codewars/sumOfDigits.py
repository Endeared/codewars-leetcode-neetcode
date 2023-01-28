# kata 6

def digital_root(n):
    nums = list(str(n))
    sum = 0
    
    for num in nums:
        sum += int(num)

    while sum > 9:
        nums = list(str(sum))
        sum = 0
        for num in nums:
            sum += int(num)
        
    return sum
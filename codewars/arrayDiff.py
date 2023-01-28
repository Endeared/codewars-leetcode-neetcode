# kata 6

def array_diff(a, b):
    final = []

    for num in a:
        if num not in b:
            final.append(num)

    return final
def displayTwice(msg):
    """Prints an inputted string twice"""
    print(msg)
    print(msg)

displayTwice("hello")
displayTwice("testing")

help(displayTwice)

def findMax(a,b):
    """Finds the maximum of two values"""
    if (a > b):
        max = a
    else:
        max = b
    return max

print(findMax(10, 53))
print(findMax(6, 2))
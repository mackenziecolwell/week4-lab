def calcAve(*numbers):
    total = 0
    for num in numbers:
        total += num
    return total/len(numbers)

print(calcAve(2, 6, 3, 8, 9, 13))
print(calcAve(4, 1, 25, 16))
print(calcAve(65, 23, 61, 95, 88, 102, 20, 33))
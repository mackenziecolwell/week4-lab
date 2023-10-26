import math

hypot = lambda a,b : math.sqrt(a * a + b * b)

print(type(hypot))

to_seconds = lambda  a,b=0 : a * 3600 + b * 60

print(to_seconds(0, 2))
print(to_seconds(2, 0))
print(to_seconds(1, 30))
print(to_seconds(1))
print(to_seconds(2))
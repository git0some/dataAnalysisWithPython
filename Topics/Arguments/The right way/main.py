#  You can experiment here, it won’t be checked
def count(a, b, c):
    return a + b - c

print(count(1, 2, 3))
print(count(1, c=2, b=3))
print(count(c=3, b=2, a=1))
#print(count(a=1, 2, c=3))
print(count(b=3, c=2, a=1))

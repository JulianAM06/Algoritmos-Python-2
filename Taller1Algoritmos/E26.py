a = 0
b = 1
c = a + b

print(a)

print(b)

print(c)

while c < 10000:

    a = b

    b = c

    c = a + b

    print(c)
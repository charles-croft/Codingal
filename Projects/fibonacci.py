import time

j = 0
a = 0
b = 1
while j==0:
    c = a+b
    print(c)
    time.sleep(0.5)
    a = b+c
    print(a)
    time.sleep(0.5)
    b = c+a
    print(b)
    time.sleep(0.5)
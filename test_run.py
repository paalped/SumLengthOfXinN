# Design an algorithms by Paal S. Pedersen
# Contact: paalped@gmail.com


import time

from calculations import slowSumStringLengthOfXinN as slow
from calculations import fastSumStringLengthOfXinN as fast

def timeItWrapper(func, n):
    t1 = time.time()
    f = func(n)
    t2 = time.time()
    return f'Calculating the sum of x in n\nlen(\'12345678910...{n}\'\n\
for x in range({n}):\n\tlength = {f}\n\ttime spent: {(t2-t1)} s\n'

if __name__ == '__main__':
    n = 999998
    s = n
    i = 0
    while True:
        n+=1
        if n < 1000000:
            print(timeItWrapper(slow, n))
            print(timeItWrapper(fast, n))
        else:
            i += 1
            n *= 100000010000001000000
            print(timeItWrapper(fast, n))
        if i > 30:
            break

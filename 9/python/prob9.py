# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
# 
# a^2 + b^2 = c^2
# For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.
# 
# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.

import math

if __name__ == "__main__":
    stop = False
    a = 1
    while not stop:
        b = a + 1
        while True:
            c = math.sqrt(a*a + b*b)
            if (a+b == 1000-c):
                print(a, b, c, a*b*c)
                stop = True
                break
            elif (c > 1000):
                break
            else:
                b+= 1
        a += 1

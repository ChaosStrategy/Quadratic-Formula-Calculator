import math
import random
import matplotlib

## a b and c value variables through user input

avalue = int(input("Please type value A:"))
bvalue = int(input("Please type value B:"))
cvalue = int(input('Please type value C:'))

xvalue1 = (0-bvalue) + math.sqrt(((bvalue*bvalue)-(4*avalue*cvalue))/(2*avalue))
xvalue2 = (0-bvalue) - math.sqrt(((bvalue*bvalue)-(4*avalue*cvalue))/(2*avalue))

print("your x intercepts are equal to ", xvalue1, " and ", xvalue2)

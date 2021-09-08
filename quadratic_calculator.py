import math
import random
import matplotlib

## a b and c value variables through user input

avalue = input("Please type value A:")
bvalue = input("Please type value B:")
cvalue = input('Please type value C:')

xvalue1 = (0-bvalue) + math.sqrt(((bvalue*bvalue)-(4*avalue*cvalue))/(2*avalue))
xvalue2 = (0-bvalue) - math.sqrt(((bvalue*bvalue)-(4*avalue*cvalue))/(2*avalue))

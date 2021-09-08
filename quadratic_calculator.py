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


## Ploimport matplotlib.pyplot as plt
# import numpy as np
# import matplotlib.pyplot as plt
#
# # create 1000 equally spaced points between -10 and 10
# x = np.linspace(-10, 10, 1000)
#
# # calculate the y value for each element of the x vector
# y = avalue*x**2 + bvalue*x + cvalue
#
# fig, ax = plt.subplots()
# ax.plot(x, y)

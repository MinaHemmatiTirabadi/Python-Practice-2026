#• Consider the polynomial 3x^2 + 2x - 1.
#• Find the roots of this function.
#• Determine the value of the function
#and its derivative at the point -2.
#Mina Hemmati

import numpy as np
coeff=np.array([3,2,-1])
f = np.poly1d(coeff)
print(np.poly1d(f))
print("==========================================")
print("The roots of the function is ", f.r)
print("==========================================")
print("The value of the function at -2 is ",np.polyval(coeff,-2))
print("==========================================")
fd=np.polyder(f,1)
print("The derivation of the function is ",np.poly1d(fd))
print("==========================================")
x=fd(-2)
print("Its derivation at the point -2 is ",x)



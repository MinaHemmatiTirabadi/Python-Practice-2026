import numpy as np
a=np.array([[2,4,2],[2,1,2],[4,1,-2]])
b=np.array([15,-5,0])
x,y,z=np.linalg.solve(a,b)
print("Solution of linear equations ",x)
print("Solution of linear equations ",y)
print("Solution of linear equations ",z)

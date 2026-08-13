#plot

import matplotlib.pyplot as plt
import numpy as np

a=np.arange((np.pi)/2,(3*(np.pi))/2,0.1)
y=1-(np.cos(a))**2

plt.plot(a,y,color="purple")
plt.grid(linestyle="--")
plt.title("1-cos(a)\u00B2",color="red")
plt.xlabel("a")
plt.ylabel("1-cos(a)\u00B2")

plt.show()

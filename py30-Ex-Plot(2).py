#plot x\u00B2+y\u00B2=1

import matplotlib.pyplot as plt
import numpy as np


x=np.arange(0,1,0.1)
y1=np.sqrt(1-(x**2))
y2=-1*(np.sqrt(1-(x**2)))


plt.plot(x,y1,color="blue")
plt.plot(x,y2,color="blue")

plt.xlabel("x")
plt.ylabel("y")

plt.title("x\u00B2+y\u00B2=1",color="red")
plt.grid(linestyle="--")

plt.show()

#Temperature and pressure chart

import matplotlib.pyplot as plt
import numpy as np

x=np.array([20,100,250,400,420,440,510])
y=np.array([120,300,700,1000,1100,1500,2000])
plt.title("Temperature and pressure chart")
plt.xlabel("Temperature")
plt.ylabel("pressure")
plt.plot(x,y,marker="o",color="red",mec="orange")
plt.show()

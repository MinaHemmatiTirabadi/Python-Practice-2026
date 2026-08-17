#Housing price chart for three districts based on floor area

import matplotlib.pyplot as plt
import numpy as np
x=np.array([40,55,60,73,89,100,110])
y1=np.array([500,710,750,890,1100,1500,1600])
y2=np.array([700,900,990,1200,1550,1800,1900])
y3=np.array([1000,1230,1400,1900,2500,3000,3700])

plt.plot(x,y1,label="Region 1",marker="o",linestyle=":",
         color="blue",mec="black")
plt.plot(x,y2,label="Region 2",marker="v",linestyle="-",
         color="pink",mec="purple")
plt.plot(x,y3,label="Region 3",marker="d",linestyle="-.",
         color="yellow",mec="orange")

plt.title("Housing price")
plt.xlabel("Meters")
plt.ylabel("Prices")

plt.legend()
plt.show()



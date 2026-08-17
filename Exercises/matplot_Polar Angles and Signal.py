#Suppose we have an antenna and
#we want to see how strong the signal is in each direction.
#Draw a polar diagram showing at what angle the antenna has the most strength.

#Distance from center = signal strength
#Angle = antenna direction

#Applications: 
#1) Mobile Antenna : Want to know: In which direction does the antenna have
#the most coverage?
#2) Radar : Want to know: At what angle is the signal best received?
#3) Speaker : They check: In which direction does the sound spread the most?
 

#Angles is theta.
#Signal is r.

import matplotlib.pyplot as plt
import numpy as np

theta = [0, 30, 60, 90, 120, 150, 180, 210, 240, 270, 300, 330]
r = [10, 12, 18, 25, 20, 13, 8, 6, 9, 15, 22, 17]
theta = np.deg2rad(theta)

fig,ax=plt.subplots(subplot_kw={"projection":"polar"})
ax.plot(theta,r)
ax.set_title("Antenna Signal Strength Pattern")
plt.show()




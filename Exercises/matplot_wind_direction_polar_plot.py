#Suppose a weather station measures wind speed in 8 directions.
#Draw a polar diagram that shows wind direction and speed simultaneously.

#Objective:
#Show wind direction on the angle.
#Put wind speed as distance from the center.
#North is at the top of the graph.

import numpy as np
import matplotlib.pyplot as plt

directions = ["N","NE","E","SE","S","SW","W","NW"]

angles = [0,45,90,135,180,225,270,315]

speed = [12,18,10,7,5,8,14,16]


d=speed.index(18)
print("The strongest wind blows from the northeast ",directions[d]," at a speed of "
      , max(speed),"m/s.")


angles = np.deg2rad(angles)

fig, ax = plt.subplots(subplot_kw={"projection":"polar"})

ax.plot(angles, speed, marker="o")

for angle, spd in zip(angles, speed):
    ax.text(angle, spd, str(spd), color="red", fontsize=12)
    
#Because on the compass, north is up.
#Move zero degrees to the top of the graph.
ax.set_theta_zero_location("N")

#In mathematics:Angles usually increase counterclockwise.
#But in a compass:Directions are clockwise
#We reverse the direction of increasing the angle.
ax.set_theta_direction(-1)

ax.set_xticks(angles)
ax.set_xticklabels(directions)

ax.set_title("Wind Speed Direction")

plt.show()



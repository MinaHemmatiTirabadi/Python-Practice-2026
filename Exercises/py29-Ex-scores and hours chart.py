#Graph of students' scores and study hours

import matplotlib.pyplot as plt
import numpy as np

x=np.array([7,17,15,12,18,19,20])#scores
y=np.array([10,12.5,13,15,17,17.5,19])#hours
colors=np.array(["red","blue","green","purple","orange","pink","black"])

plt.ylabel("scores")
plt.xlabel("houres")


plt.title("students' scores and study hours")

plt.scatter(y,x,c=colors)

plt.show()

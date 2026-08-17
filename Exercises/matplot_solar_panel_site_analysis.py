#A company wants to install solar panels in a mountainous area.

#For each point on the ground, two factors are important:

#Slope
#High slope → more difficult installation and lower efficiency
#Low slope → more suitable
#Solar Radiation
#High radiation → more energy production

#Objective:
#Using Contour Plot, create a map that identifies the best areas
#for installing solar panels.

import numpy as np
import matplotlib.pyplot as plt


# Land position
x = np.arange(0, 7)
y = np.arange(0, 7)


# Land slope (degree)
slope = np.array([
    [5,  7, 10, 15, 20, 25, 30],
    [4,  6, 12, 18, 22, 28, 35],
    [3,  5, 15, 20, 30, 36, 40],
    [2,  8, 14, 25, 32, 38, 45],
    [1,  6, 12, 22, 28, 35, 42],
    [3,  5, 10, 18, 24, 30, 37],
    [4,  8, 13, 17, 23, 27, 33]
])


# Solar radiation (kWh/m²)
solar = np.array([
    [900, 950, 980, 1000, 1050, 1100, 1150],
    [850, 920, 970, 1030, 1080, 1140, 1200],
    [800, 880, 960, 1050, 1120, 1180, 1250],
    [780, 850, 940, 1020, 1100, 1160, 1220],
    [760, 830, 900, 980, 1060, 1130, 1190],
    [740, 800, 870, 950, 1020, 1080, 1150],
    [700, 780, 850, 920, 990, 1050, 1100]
])


# Building a Land Suitability Score
def suitability_score(solar, slope):
    return solar - 10 * slope


# Constructing a coordinate grid
X, Y = np.meshgrid(x, y)


# Calculating points
Z = suitability_score(solar, slope)


# Finding the best spot
best = np.unravel_index(np.argmax(Z), Z.shape)

best_x = x[best[1]]
best_y = y[best[0]]
best_score = Z[best]


print("Best location:")
print("X =", best_x)
print("Y =", best_y)
print("Score =", best_score)


# -------------------------
# Drawing a 3D diagram
# -------------------------

fig = plt.figure(figsize=(10, 7))

ax = fig.add_subplot(111, projection="3d")


surface = ax.plot_surface(
    X,
    Y,
    Z,
    cmap="viridis",
    edgecolor="black"
)


# Show the best spot
ax.scatter(
    best_x,
    best_y,
    best_score,
    color="red",
    s=100
)


# Axis labels
ax.set_xlabel("East-West Position")
ax.set_ylabel("North-South Position")
ax.set_zlabel("Suitability Score")


ax.set_title("Solar Panel Site Suitability 3D Surface")


# Viewing angle rotation
ax.view_init(
    elev=35,
    azim=45
)


# Color bar
fig.colorbar(surface, shrink=0.5)


plt.show()













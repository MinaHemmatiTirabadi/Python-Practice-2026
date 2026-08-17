# 3D visualization of a mathematical function
# Plot three different 3D graphs (wireframe, scatter, and surface)
# based on X, Y, and Z coordinates.
#
# Domain:
# -3 <= x <= 3
# -2 <= y <= 2
#
# Functions:
# z1 = exp(-x² - y²)
# z2 = exp(-((x-1)² + (y-1)²))
#
# Calculate:
# Z = (z1 - z2)²
#
# Libraries used:
# NumPy for numerical calculations
# Matplotlib for 3D visualization


#Mina Hemmati

import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots(1, 3, figsize=(15,5),
                       subplot_kw={'projection': '3d'})
fig.suptitle(r"3D of $Z=(z_1-z_2)^2$", fontsize=16)

x = np.linspace(-3, 3, 100)
y = np.linspace(-2, 2, 100)

X, Y = np.meshgrid(x, y)

Z1 = np.exp(-X**2 - Y**2)
Z2 = np.exp(-(X-1)**2 - (Y-1)**2)

Z = (Z1 - Z2)**2


ax[0].plot_wireframe(X[::5, ::5], Y[::5, ::5], Z[::5, ::5],color="green")
ax[0].set_title("Wireframe")

ax[1].scatter3D(X[::5, ::5], Y[::5, ::5], Z[::5, ::5],color="blue")
ax[1].set_title("Scatter")

ax[2].plot_surface(X[::5, ::5], Y[::5, ::5], Z[::5, ::5],color="red")
ax[2].set_title("Surface")


plt.show()

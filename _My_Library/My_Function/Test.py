import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
from Calculate import listX, listY, listZ, linInterp3D

# Example data
x = listX
y = listY
z = listZ

# Convert the lists to numpy arrays
x = np.array(x)
y = np.array(y)
z = np.array(z)

# Create a meshgrid from x and y
X, Y = np.meshgrid(x, y)

# Create a 3D plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plot the surface
surf = ax.plot_surface(X, Y, z, cmap='viridis')

# Add labels and a colorbar
ax.set_xlabel('$m_{ef}$')
ax.set_ylabel(r'$\overline{\lambda}$')
ax.set_zlabel('$φ_{ex}$')
fig.colorbar(surf, ax=ax, shrink=0.5, aspect=10)

# Show the plot
plt.show()
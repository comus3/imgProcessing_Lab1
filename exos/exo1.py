import numpy
import matplotlib

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

x = [1, -1, -1, 1, 1, 1, -1, -1, 1, 1, -1, -1, -1, -1, 1, 1]
y = [1, 1, -1, -1, 1, 1, 1, -1, -1, 1, 1, 1, -1, -1, -1, -1]
z = [1, 1, 1, 1, 1, -1, -1, -1, -1, -1, -1, 1, 1, -1, -1, 1]

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

edges = [
    [0, 1], [1, 2], [2, 3], [3, 0],
    [4, 5], [5, 6], [6, 7], [7, 4],
    [0, 4], [1, 5], [2, 6], [3, 7]
]

for edge in edges:
    ax.plot([x[edge[0]], x[edge[1]]], [y[edge[0]], y[edge[1]]], [z[edge[0]], z[edge[1]]])

#labels
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

#limites
ax.set_xlim([-2, 2])
ax.set_ylim([-2, 2])
ax.set_zlim([-2, 2])

plt.show()

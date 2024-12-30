import numpy as np
import matplotlib.pyplot as plt
from scipy.spatial import Voronoi, voronoi_plot_2d


points = np.array([
    [5, 1], [7, -1], [9, -1], [7, 3], [11, 1], [9, 3],  # A1 to A6
    [3, 0], [13, 0]  # A7, A8
])


vor = Voronoi(points)


fig, ax = plt.subplots(figsize=(8, 8))
voronoi_plot_2d(vor, ax=ax)
ax.scatter(points[:, 0], points[:, 1], color='red', label='Points')
ax.set_title("Voronoi Diagram with 4 Half-Lines")
ax.legend()
plt.show()

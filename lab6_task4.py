import numpy as np
from scipy.spatial import Voronoi, voronoi_plot_2d
import matplotlib.pyplot as plt


points_A = [(1 + i, i - 1) for i in range(6)]
points_B = [(-i, i) for i in range(6)]
points_C = [(0, i) for i in range(6)]
points = np.array(points_A + points_B + points_C)


vor = Voronoi(points)


half_lines = 0
for ridge in vor.ridge_vertices:
    if -1 in ridge:
        half_lines += 1

print(f"Number of half-lines in the Voronoi diagram: {half_lines}")


fig = voronoi_plot_2d(vor, show_vertices=False, line_colors='orange', line_width=2)
plt.plot(points[:, 0], points[:, 1], 'o', color='blue')
plt.xlim(-10, 15)
plt.ylim(-5, 10)
plt.gca().set_aspect('equal', adjustable='box')
plt.title("Voronoi Diagram")
plt.show()

import numpy as np
import matplotlib.pyplot as plt
from scipy.spatial import Delaunay, Voronoi, voronoi_plot_2d

# Step 1: Define the two sets of points
M1 = np.array([
    [0, 0], [2, 0], [1, 1], [3, 1], [1.5, 2]
])  # 5 points

M2 = np.array([
    [0, 0], [2, 0], [1, 1], [3, 1], [1.5, 2], [2, 2]
])  # 6 points

# Step 2: Compute Delaunay Triangulations and Voronoi Diagrams
tri_M1 = Delaunay(M1)
tri_M2 = Delaunay(M2)
vor_M1 = Voronoi(M1)
vor_M2 = Voronoi(M2)


def plot_triangulation_and_voronoi(points, triangulation, voronoi, title):
    fig, ax = plt.subplots(1, 2, figsize=(12, 6))


    ax[0].triplot(points[:, 0], points[:, 1], triangulation.simplices, color='blue')
    ax[0].scatter(points[:, 0], points[:, 1], color='red')
    ax[0].set_title(f"Delaunay Triangulation - {title}")
    ax[0].axis('equal')


    voronoi_plot_2d(voronoi, ax=ax[1], show_vertices=False, line_colors='orange', line_width=2)
    ax[1].scatter(points[:, 0], points[:, 1], color='red')
    ax[1].set_title(f"Voronoi Diagram - {title}")
    ax[1].axis('equal')

    plt.show()


plot_triangulation_and_voronoi(M1, tri_M1, vor_M1, "M1")
plot_triangulation_and_voronoi(M2, tri_M2, vor_M2, "M2")

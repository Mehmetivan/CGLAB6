import numpy as np
import matplotlib.pyplot as plt
from scipy.spatial import Delaunay



def generate_points(lambda_value):

    points = np.array([
        [1, -1],  # A
        [-1, 1],  # B
        [2, -1],  # C
        [1, 1],  # D
        [0, 2],  # E
        [1, lambda_value]  # M = (1, λ)
    ])
    return points



def triangulate_and_count(lambda_value):
    # Generate points with given λ
    points = generate_points(lambda_value)


    tri = Delaunay(points)

    # Count number of triangles and edges
    num_triangles = len(tri.simplices)
    num_edges = len(
        set([tuple(sorted(edge)) for simplex in tri.simplices for edge in zip(simplex, np.roll(simplex, 1))]))

    return num_triangles, num_edges, points, tri



def plot_triangulation(points, tri, lambda_value):
    plt.figure(figsize=(6, 6))
    plt.triplot(points[:, 0], points[:, 1], tri.simplices, color='blue', alpha=0.5)
    plt.plot(points[:, 0], points[:, 1], 'ro')  # Plot the points
    plt.title(f"Triangulation for λ = {lambda_value}")
    plt.gca().set_aspect('equal', adjustable='box')
    plt.show()



for lambda_value in np.linspace(-10, 10, 21):
    num_triangles, num_edges, points, tri = triangulate_and_count(lambda_value)

    print(f"For λ = {lambda_value}:")
    print(f"  Number of triangles: {num_triangles}")
    print(f"  Number of edges: {num_edges}")



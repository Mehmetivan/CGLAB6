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



def plot_individual_triangulations(lambda_values):
    for lambda_value in lambda_values:

        points = generate_points(lambda_value)
        tri = Delaunay(points)


        plt.figure(figsize=(6, 6))
        plt.triplot(points[:, 0], points[:, 1], tri.simplices, color='blue', alpha=0.5)
        plt.plot(points[:, 0], points[:, 1], 'ro')  # Plot the points
        plt.title(f"Triangulation for λ = {lambda_value}")
        plt.gca().set_aspect('equal', adjustable='box')
        plt.show()



lambda_values = [4.0, 3.0, 1.0, -1.0, -3.0, -4.0]


plot_individual_triangulations(lambda_values)

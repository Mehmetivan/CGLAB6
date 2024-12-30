import numpy as np
from scipy.spatial.distance import pdist, squareform
import networkx as nx


fixed_points = np.array([
    [1, 6],  # A
    [1, 1],  # B
    [-4, 7],  # C
    [6, 7],  # D
    [1, -1],  # E
    [5, 3],  # F
    [-2, 3]  # P
])


def calculate_mst_length(lambda_value):

    Q = np.array([lambda_value - 2, 3])
    points = np.vstack([fixed_points, Q])  # Combine fixed points with Q


    distances = squareform(pdist(points))


    G = nx.Graph()
    for i in range(len(points)):
        for j in range(i + 1, len(points)):
            G.add_edge(i, j, weight=distances[i, j])

    mst = nx.minimum_spanning_tree(G)
    mst_length = sum(edge[2]['weight'] for edge in mst.edges(data=True))
    return mst_length



lambda_values = np.linspace(-10, 10, 100)  # Range of lambda values
mst_lengths = [calculate_mst_length(l) for l in lambda_values]

min_lambda = lambda_values[np.argmin(mst_lengths)]
min_length = min(mst_lengths)

print(f"Minimum MST length: {min_length:.2f} at λ = {min_lambda:.2f}")


import matplotlib.pyplot as plt

plt.plot(lambda_values, mst_lengths, label="MST Length")
plt.xlabel("λ")
plt.ylabel("MST Length")
plt.title("MST Length vs λ")
plt.axvline(min_lambda, color='red', linestyle='--', label=f"Min λ = {min_lambda:.2f}")
plt.legend()
plt.show()

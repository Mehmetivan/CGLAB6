import numpy as np
from scipy.spatial import distance
from scipy.sparse.csgraph import minimum_spanning_tree

# Define fixed points
points = {
    "A": (1, 6),
    "B": (1, 1),
    "C": (-4, 7),
    "D": (6, 7),
    "E": (1, -1),
    "F": (5, 3),
    "P": (-2, 3),
}

# Function to compute MST length for a given lambda
def compute_mst_length(lambda_val):
    Q = (lambda_val - 2, 3)  # Define Q's position
    all_points = list(points.values()) + [Q]
    # Compute pairwise distances
    dist_matrix = distance.cdist(all_points, all_points, metric="euclidean")
    # Compute MST using SciPy
    mst = minimum_spanning_tree(dist_matrix)
    return mst.toarray().sum()  # Return the MST total weight

# Find the lambda that minimizes the MST length
lambda_values = np.linspace(-10, 10, 1000)  # Range of lambda values to test
mst_lengths = [compute_mst_length(l) for l in lambda_values]
min_lambda = lambda_values[np.argmin(mst_lengths)]
min_mst_length = min(mst_lengths)

# Output the results
print(f"The optimal lambda is: {min_lambda:.2f}")
print(f"The minimal MST length is: {min_mst_length:.2f}")

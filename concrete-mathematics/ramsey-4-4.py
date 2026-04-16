import itertools
import numpy as np
import random
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

def generate_random_regular_graph(n=17, red_degree=8):
    """
    Generates a 17x17 adjacency matrix where every node has 
    exactly 8 red edges (1) and 8 blue edges (0).
    """
    adj = np.zeros((n, n), dtype=int)
    
    # In a circulant graph K_17, offsets are 1 through 8.
    # To get a degree of 8, we pick 4 offsets (each offset adds 2 edges: +o and -o).
    all_offsets = list(range(1, (n // 2) + 1))
    red_offsets = random.sample(all_offsets, red_degree // 2)
    
    for i in range(n):
        for o in red_offsets:
            j1 = (i + o) % n
            j2 = (i - o) % n
            adj[i][j1] = 1
            adj[j1][i] = 1
            adj[i][j2] = 1
            adj[j2][i] = 1
            
    # Optional: Randomly permute the nodes to increase 'randomness'
    # while preserving the degree properties.
    perm = np.random.permutation(n)
    adj = adj[perm, :][:, perm]
    
    return adj

def detect_4_cliques(matrix):
    """
    Detects if a 17x17 matrix has a 4-red or 4-blue clique.
    Matrix: 0 for blue, 1 for red.
    """
    nodes = range(len(matrix))
    # Check all combinations of 4 nodes
    for combo in itertools.combinations(nodes, 4):
        red_edges = 0
        blue_edges = 0
        total_pairs = 0
        
        # Check all pairs within the 4 nodes
        for i, j in itertools.combinations(combo, 2):
            total_pairs += 1
            if matrix[i][j] == 1:
                red_edges += 1
            else:
                blue_edges += 1
        
        # 4-red-clique: all 6 edges are 1
        if red_edges == 6:
            return True, combo
        # 4-blue-clique: all 6 edges are 0
        if blue_edges == 6:
            return True, combo
            
    return False, None


def visualize_colored_graph(matrix):
    n = len(matrix)
    G = nx.Graph()
    
    # Add nodes
    G.add_nodes_from(range(n))
    
    # Define edge lists based on matrix values
    red_edges = []
    blue_edges = []
    
    for i in range(n):
        for j in range(i + 1, n):  # Undirected: only check upper triangle
            if matrix[i][j] == 0:
                red_edges.append((i, j))
            else:
                blue_edges.append((i, j))
    
    # Position nodes in a circle for clarity with 17 nodes
    pos = nx.circular_layout(G)
    
    plt.figure(figsize=(10, 10))
    
    # Draw nodes
    nx.draw_networkx_nodes(G, pos, node_size=500, node_color='lightgrey')
    nx.draw_networkx_labels(G, pos, font_size=10, font_family='sans-serif')
    
    # Draw edges with specific colors
    nx.draw_networkx_edges(G, pos, edgelist=red_edges, edge_color='red', width=1.5, alpha=0.7)
    nx.draw_networkx_edges(G, pos, edgelist=blue_edges, edge_color='blue', width=1.5, alpha=0.7)
    
    plt.title(f"Complete Graph ($K_{{{n}}}$) with Matrix-Defined Edge Colors")
    plt.axis('off')
    plt.show()


# Example Usage:
# Create a dummy 17x17 matrix (0 or 1)
np.random.seed(42)

result = True
while result:
    adj_matrix = generate_random_regular_graph()
    np.fill_diagonal(adj_matrix, 0) # No self-loops
    result, nodes = detect_4_cliques(adj_matrix)
    if not result:
        print("no cliques found for ", adj_matrix)
        visualize_colored_graph(adj_matrix)
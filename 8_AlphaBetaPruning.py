import math

def abpruning(node, depth, alpha, beta, maxp, branches, values, parent_node='Root'):
    """
    Implements the Alpha-Beta Pruning algorithm, tracks the optimal path,
    and prints the nodes that are pruned.

    Args:
        node (str): The current node identifier.
        depth (int): The remaining depth to search.
        alpha (float): The best value found so far for the Maximizer.
        beta (float): The best value found so far for the Minimizer.
        maxp (bool): True if the current player is maximizing.
        branches (dict): Mapping of intermediate nodes to their children.
        values (dict): Mapping of leaf nodes to their utility values.
        parent_node (str): The parent of the current node (for logging purposes).

    Returns:
        tuple: (optimal_value, optimal_path_list)
    """

    # 🛑 Base Case: Reached a leaf node or maximum search depth
    if depth == 0 or node in values:
        # Returns the utility value and the path (which is just the node itself)
        return values.get(node, 0), [node]

    # Initialize variables for tracking the best move and path
    best_path = []

    if maxp:
        max_eval = -math.inf

        for child in branches[node]:
            # Recursive call
            eval, path = abpruning(child, depth - 1, alpha, beta, False, branches, values, node)

            if eval > max_eval:
                max_eval = eval
                # The best path starts at the current node, followed by the path from the child
                best_path = [node] + path

            alpha = max(alpha, max_eval)

            if beta <= alpha:
                # ✂️ BETA CUT-OFF
                print(f"❌ **PRUNED**: Node '{child}' and its remaining siblings under '{node}'.")
                print(f"   (Reason: Beta Cut-off, since β={beta} <= α={alpha})")
                break # Beta cut-off

        return max_eval, best_path

    else: # Minimizing player
        min_eval = math.inf

        for child in branches[node]:
            # Recursive call
            eval, path = abpruning(child, depth - 1, alpha, beta, True, branches, values, node)

            if eval < min_eval:
                min_eval = eval
                # The best path starts at the current node, followed by the path from the child
                best_path = [node] + path

            beta = min(beta, min_eval)

            if beta <= alpha:
                # ✂️ ALPHA CUT-OFF
                print(f"❌ **PRUNED**: Node '{child}' and its remaining siblings under '{node}'.")
                print(f"   (Reason: Alpha Cut-off, since β={beta} <= α={alpha})")
                break # Alpha cut-off

        return min_eval, best_path

# --- Example Game Tree Data ---

print("=" * 60)
print("Starting Alpha-Beta Pruning Search with Cut-off Tracking")
print("=" * 60)

# Defines the structure of the tree (intermediate nodes to children)
branches = {
    'A': ['B', 'C'], # Root (Maximizer)
    'B': ['D', 'E'], # Minimizer
    'C': ['F', 'G']  # Minimizer
}

# Defines the leaf node utility values
values = {
    'D': 3, 'E': 9,
    'F': 1, 'G': 0,
}

# --- Execution ---

# Note: The depth is 3 because the values are 3 levels down from 'A'
optimal_value, optimal_path_nodes = abpruning(
    'A', 3, -math.inf, math.inf, True, branches, values
)

print("\n" + "=" * 60)
print("✨ FINAL RESULT ✨")
print("=" * 60)
print(f"The Optimal Value is: {optimal_value}")
print(f"The Optimal Path is: {' -> '.join(optimal_path_nodes)}")
print(f"The best immediate move from 'A' is to: {optimal_path_nodes[1]}")
print("=" * 60)
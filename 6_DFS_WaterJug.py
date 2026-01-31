class Node:
    def __init__(self, value):
        self.value = value
        self.children = []

# DFS using stack
def dfs_stack(root):
    if not root:
        return

    stack = [root]
    visited = set()

    while stack:
        current = stack.pop()

        if current in visited:
            continue

        visited.add(current)
        print(current.value, end=" ")

        # Push children in reverse so leftmost child prints first
        for child in reversed(current.children):
            stack.append(child)


# Create Nodes
A = Node("(0,0)")
B = Node("(0,3)")
C = Node("(3,0)")
D = Node("(3,3)")
E = Node("(4,2)")
F = Node("(0,2)")
G = Node("(2,0)")


# Build the tree
A.children = [B]
B.children = [C]
C.children = [D]
D.children = [E]
E.children = [F]
F.children = [G]

print("DFS Traversal of the Tree:")
dfs_stack(A)

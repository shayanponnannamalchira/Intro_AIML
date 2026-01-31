class Node:
    def __init__(self, value):
        self.value = value
        self.children = []      # List of child nodes

from collections import deque

def bfs(root):
    if not root:
        return
    
    queue = deque([root])      # Initialize queue with root

    while queue:
        current_node = queue.popleft()
        print(current_node.value, end=" ")

        # Enqueue all children of current node
        for child in current_node.children:
            queue.append(child)


# Create Nodes
A = Node("(0,0)")
B = Node("(0,3)")
C = Node("(3,0)")
D = Node("(3,3)")
E = Node("(4,2)")
F = Node("(0,2)")
G = Node("(2,0)")

# Build the tree
A.children = [B, C, D]
B.children = [E]
C.children = [F]
D.children = [G]

print("BFS Traversal of the Tree:")
bfs(A)

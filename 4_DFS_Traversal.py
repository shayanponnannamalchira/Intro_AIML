class Node:
    def __init__(self, value):
        self.value = value
        self.children = []


def dfs(root):
    if not root:
        return

    stack = [root]

    while stack:
        current_node = stack.pop()
        print(current_node.value, end=" ")

        # Push children in reverse so the leftmost child prints first
        for child in reversed(current_node.children):
            stack.append(child)

A = Node("A")
B = Node("B")
C = Node("C")
D = Node("D")
E = Node("E")
F = Node("F")

# Build the tree
A.children = [B, C, D]
B.children = [E]
D.children = [F]

print("DFS Traversal of the tree:")
dfs(A)

class Node:
    def __init__(self, value):
        self.value = value
        self.children = []


# DFS Traversal using Stack
def dfs(root):
    if not root:
        return

    stack = [root]

    while stack:
        current_node = stack.pop()
        print(current_node.value, end=" ")

        # Push children in reverse so the leftmost prints first
        for child in reversed(current_node.children):
            stack.append(child)


# DFS Search
def dfs_search(root, target):
    if not root:
        return None

    stack = [root]

    while stack:
        current_node = stack.pop()
        print(f"Visiting : {current_node.value}")

        # If value matches, found
        if current_node.value == target.value:
            print(f"Node '{target.value}' found.")
            return current_node

        # Push children (reversed)
        for child in reversed(current_node.children):
            stack.append(child)

    print(f"Node '{target.value}' not found.")
    return None

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

print("\n\nSearching in tree using DFS:")
result = dfs_search(A, E)

if result:
    print(f"Search successful : Node '{result.value}' exists.")
else:
    print("Search unsuccessful")

a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)
e = Node(5)
f = Node(6)

# Build the tree
a.children = [b, c, d]
b.children = [e]
c.children = [f]

print("\nDFS Traversal of the tree:")
dfs(a)

print("\n\nSearching in tree using DFS:")
result = dfs_search(a, f)   

if result:
    print(f"Search successful : Node '{result.value}' exists.")
else:
    print("Search unsuccessful")

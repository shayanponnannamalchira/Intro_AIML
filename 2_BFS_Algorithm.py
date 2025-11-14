class Node:
    def __init__(self, value):   
        self.value = value
        self.children = []

from collections import deque

def bfs(root, target):
    if not root:
        return None
    queue = deque([root])
    while queue:
        current_node = queue.popleft()
        print(f"visiting:{current_node.value}")
        if current_node.value == target:
            print(f"Node'{target}'found.")
            return current_node
        for child in current_node.children:
            queue.append(child)
        print(f"NOde'{target}'not found.")
    return None

# Create nodes (Strings)
A = Node('A')
B = Node('B')
C = Node('C')
D = Node('D')
E = Node('E')
F = Node('F')

# Build the tree (link objects, not strings)
A.children = [B, C, D]
B.children = [E]
D.children = [F]

print("Searching in tree using BFS:")
result = bfs(A, 'E')
if result:
    print(f"Serach successful:Node'{result.value}'exists.")
else:
    print("Search unsuccessful.")
print("")

# For Numbers
A = Node('1')
B = Node('2')
C = Node('3')
D = Node('4')
E = Node('5')
F = Node('6')

A.children = [B, C, D]
B.children = [E]
D.children = [F]

print("Searching in tree using BFS (numbers):")
result = bfs(A, '5')
if result:
    print(f"Serach successful:Node'{result.value}'exists.")
else:
    print("Search unsuccessful.")

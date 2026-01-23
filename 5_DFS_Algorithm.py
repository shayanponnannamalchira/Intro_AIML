#Depth First Search (DFS) implementation in Python
class Node:
    def __init__(self, value):
        self.value = value
        self.child = []
def dfs(root, target):
    if root is None:
        return

    stack = [root]

    while stack:
        current = stack.pop()
        if current.value == target:
            print(f"Target {target} found!")
            return current
        for child in reversed(current.child):
            stack.append(child)
    return None

root = Node('A')
B = Node('B')
C = Node('C')
D = Node('D')
E = Node('E')
F = Node('F')
root.child = [B, C, D]
B.child = [E]
D.child = [F]
print("\nSearching in tree using DFS:")
result = dfs(root, 'E')
if result:
    print(f"Search successful: Node '{result.value}' exists in the tree.")
else:
    print("Search unsuccessful: Node not found in the tree.")
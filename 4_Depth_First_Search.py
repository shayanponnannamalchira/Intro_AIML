#traversing a tree using DFS
class Node:
    def __init__(self, value):   
        self.value = value
        self.children = []
def dfs(root):
    if root is None:
        return
    stack=[root]
    while stack:
        current_node=stack.pop()
        print(current_node.value,end=" ")
        for child in reversed(current_node.children):
            stack.append(child)
root=Node('A')
B=Node('B')
C=Node('C')
D=Node('D')
E=Node('E')
F=Node('F')
root
B.children=[E]
D.children=[F]
print("DFS Traversal of the tree:")
dfs(root)

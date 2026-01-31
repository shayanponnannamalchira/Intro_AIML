class Node:
    def __init__(self, value):
        self.value = value
        self.children = []

from collections import deque
def bfs(root):
    if not root:
        return
    queue=deque([root])
    while queue:
        current_node=queue.popleft()
        print(current_node.value,end="")
        for child in current_node.children:
            queue.append(child)
            
#create Nodes
A=Node("A")
B=Node("B")
C=Node("C")
D=Node("D")
E=Node("E")
F=Node("F")

#Build the tree
A.children=[B,C,D]
B.children=[E]
C.children=[F]
print("BFS Traversal of the tree:")
bfs(A)

#create nodes using Integer Values
a=Node(1)
b=Node(2)
c=Node(3)
d=Node(4)
e=Node(5)
f=Node(6)

#Build the tree
a.children=[b,c,d]
b.children=[e]
c.children=[f]
print("\nBFS Traversal of the tree with Integer values:")
bfs(a)
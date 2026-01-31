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
            
def bfs_search(root, target):
    if not root:
        return None
    queue=deque([root])
    while queue:
        current_node=queue.popleft()
        print(f"Visiting Node: {current_node.value}")
        if current_node.value == target:
            print(f"Target {target} found!")
            return current_node
        for child in current_node.children:
            queue.append(child)
    print(f"Target {target} not found in the tree.")
    return None

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

#Searching tree
print("\n Searching in tree using BFS:")
result=bfs_search(A, "E")
if result:
    print(f"Search successful:Node'{result.value}' exists.")
else:
    print("Search unsuccessful:Node does not exist.")
    
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

#Searching tree 
print("\n Searching in tree with Integer values using BFS:")
result=bfs_search(a, b)
if result:
    print(f"Search successful:Node'{result.value}' exists.")
else:
    print("Search unsuccessful:Node does not exist.")
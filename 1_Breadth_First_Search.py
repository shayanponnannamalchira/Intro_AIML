#traversing a tree using BFS
#Queue data structure is used to implement BFS
class Node:
    def __init__(self, value):   # Corrected here
        self.value = value
        self.children = []

from collections import deque

def bfs(root):
    if not root:
        return

    queue = deque()
    queue.append(root)
    
    while queue:
        current_node = queue.popleft()
        print(current_node.value, end=" ")
        
        for child in current_node.children:
            queue.append(child)

#Create nodes
A = Node('A')
B = Node('B')
C = Node('C')
D = Node('D')
E = Node('E')
F = Node('F')

#Build the tree
A.children = [B, C, D]
B.children = [E]
D.children = [F]

print("BFS Traversal of the tree:")
bfs(A)


class Node:
    def __init__(self, value):   
        self.value = value
        self.children = []

from collections import deque

def bfs(root):
    if not root:
        return

    queue = deque()
    queue.append(root)
    
    while queue:
        current_node = queue.popleft()
        print(current_node.value, end=" ")
        
        for child in current_node.children:
            queue.append(child)

#Create nodes
node1 = Node('1')
node2 = Node('2')
node3 = Node('3')
node4 = Node('4')
node5 = Node('5')
node6 = Node('6')

node1.children = [node2, node3, node4]
node2.children = [node5]
node4.children = [node6]

print("BFS Traversal of the tree:")
bfs(node1)
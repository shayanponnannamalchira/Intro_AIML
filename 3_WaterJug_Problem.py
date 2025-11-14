class node: 
    def _init_(self,value):
        self.value=value
        self.children=[]
        
from collections import deque

def bfs_search(root,target):
    if not root:
        return None
    
    queue=deque([root])
    while queue: 
        current_node=queue.popleft()
        print(f"Visiting :{current_node.value}")
        if current_node.value==target:
            print(f"none'{target}'found.")
            return current_node
        for child in current_node.children:
            queue.append(child)

    print(f"node'{target}' not found.")
    return None
node1=node('1')
node2=node('2')
node3=node('3')
node4=node('4')
node5=node('5')
node6=node('6')

node88 = node('88')
node87 = node('87')
node99 = node('99')
node8 = node('8')
node7 = node('7')

node1.children = [node88, node87, node99, node2, node5]
node2.children = [node8]
node5.children = [node7]

print("Searching in tree using bfs:")
result=bfs_search(node1,'99')
    
if result:
        print(f"search successful: node'{result.value}'exists.")
else: 
        print("search unsuccessful.")
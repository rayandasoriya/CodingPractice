class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None


def insert(root,node):
    if root is None:
        root = node
    else:
        if root.data<node.data:
            if root.right is None:
                root.right = node
            else:
                insert(root.right, node)
        else:
            if root.left is None:
                root.left = node
            else:
                insert(root.left, node)
def inorder(root):
    if root:
        inorder(root.left)
        print(root.data)
        inorder(root.right)
r = Node(50)
insert(r,Node(12))
insert(r,Node(42))
insert(r,Node(13))
inorder(r)



            

            

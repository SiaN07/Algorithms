#Using recursion
#Tree transversals

class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

def printInorder(root):
    if root:
        printInorder(root.left)
        print(root.val),
        printInorder(root.right)
        
def printPreorder(root):
    if root:
        print(root.val),
        printPreorder(root.left)
        printPreorder(root.right)
        
def printPostorder(root):
    if root:
        printPostorder(root.left)
        printPostorder(root.right)
        print(root.val),
        
#Driver code 
root = Node(25)
root.left = Node(15)
root.left.left = Node(10)
root.left.left.left = Node(4)
root.left.left.right = Node(12)
root.left.right = Node(22)
root.left.right.left = Node(18)
root.left.right.right = Node(24)
root.right = Node(50)
root.right.left = Node(35)
root.right.left.left = Node(31)
root.right.left.right = Node(44)
root.right.right = Node(70)
root.right.right.left = Node(66)
root.right.right.right = Node(90)

print ("Preorder traversal of binary tree is")
printPreorder(root) 
  
print ("\nInorder traversal of binary tree is")
printInorder(root)
  
print ("\nPostorder traversal of binary tree is")
printPostorder(root)

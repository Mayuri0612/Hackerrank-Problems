'''
Algorithm Inorder(tree)
   1. Traverse the left subtree, i.e., call Inorder(left-subtree)
   2. Visit the root.
   3. Traverse the right subtree, i.e., call Inorder(right-subtree)

'''
class Node: 
    def __init__(self,key): 
        self.left = None
        self.right = None
        self.val = key 

def inOrder(root):
    #Write your code here
    if root:
        inOrder(root.left)
        print(root.info, sep=' ', end=' ')
        inOrder(root.right)

if __name__ == "__main__":
    root = Node(1) 
    root.left      = Node(2)
    root.right     = Node(3) 
    root.left.left  = Node(4) 
    root.left.right  = Node(5) 

    print "\nInorder traversal of binary tree is"
    inOrder(root) 
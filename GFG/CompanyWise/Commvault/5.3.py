#Given postorder and in order of BT, fing its preorder
class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class ConstructTree:
    def postin(self, post, inor):
        if len(inor) == 0:
            return None
        else:

            node = TreeNode(post[-1])
            ind = inor.index(post[-1])

            node.right = self.postin(post[ind:len(post)-1], inor[ind+1:])
            node.left = self.postin(post[0:ind], inor[0:ind])
            return node

def preorder(root):
    if root is None:
        return 0
    else:
        print(root.data, end = " ")
        preorder(root.left)
        preorder(root.right)
        

ob = ConstructTree()
post = [4,5,2,6,3,1]
inor = [4,2,5,1,3,6]
tree1 = ob.postin(post, inor)
print("Post order sequence : ", end = " ")
tree2 = preorder(tree1)

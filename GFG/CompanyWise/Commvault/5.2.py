#Given preorder and in order of BT, fing its postorder
class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class ConstructTree:
    def prein(self, pre, inor):
        if not pre:
            return None
        else:

            node = TreeNode(pre[0])
            ind = inor.index(pre[0])

            node.left = self.prein(pre[1:ind+1], inor[0:ind])
            node.right = self.prein(pre[ind+1:], inor[ind+1:])
            return node

def postorder(root):
    if root is None:
        return 0
    else:
        postorder(root.left)
        postorder(root.right)
        print(root.data, end = " ")

ob = ConstructTree()
pre = [3,9,20,15,7]
inor = [9,3,15,20,7]
tree1 = ob.prein(pre, inor)
print("Post order sequence : ", end = " ")
tree2 = postorder(tree1)

#Given preorder and post order of BT, fing its inorder
class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
'''
def height(node):
    if node is None:
        return 0
    else:
        l = height(node.left)
        r = height(node.right)
        if l > r:
            return l+1
        if r > l:
            return r+1

def levels(root):
    print('Binary tree is [', end = " ")
    h = height(root)
    for i in range(1, h+1):
        if root is None:
            return 0
        if level == 1:
            print(root.data, end = " ")
        if level > 1:
            levels(root.left, level - 1)
            levels(root.right, level - 1)

    print(']')
'''
class ConstructTree:
    def prepost(self, pre, post):
        if not pre:
            return None
        if len(pre) == 1:
            return TreeNode(post.pop())
        if len(pre) > 1:
            node = TreeNode(post.pop())
            ind = pre.index(post[-1])

            node.right = self.prepost(pre[ind:], post)
            node.left = self.prepost(pre[1:ind], post)
            return node

def inorder(root):
    if root is None:
        return 0
    else:
        inorder(root.left)
        print(root.data)
        inorder(root.right)

ob = ConstructTree()
pre = [1,2,4,5,3,6,7]
post = [4,5,2,6,7,3,1]
tree1 = ob.prepost(pre, post)
tree2 = inorder(tree1)
#levels(tree)


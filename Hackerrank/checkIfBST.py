INT_MIN = -4294967296
INT_MAX = 4294967296

def checkBST(root):
        return helper(root, INT_MIN, INT_MAX)
    
def helper(root, minval, maxval):
    if root is None:
        return True
    if(root.data > maxval or root.data < minval):
        return False
    return(helper(root.left, minval, root.data - 1) and helper(root.right, root.data + 1, maxval))
    
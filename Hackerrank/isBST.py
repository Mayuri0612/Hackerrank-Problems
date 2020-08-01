INT_MAX = 4294967296
INT_MIN = -4294967296
def check_binary_search_tree_(root):
    return (hf(root, INT_MIN, INT_MAX)) 

def hf(root, min, max): 
    if root is None: 
        return True
    if root.data < min or root.data > max: 
        return False
    return (hf(root.left, min, root.data -1) and
          hf(root.right, root.data+1, max)) 
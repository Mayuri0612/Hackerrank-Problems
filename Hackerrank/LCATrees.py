def lca(root, v1, v2):
    current = root.info
    if root is None:
        return None
    if(current > v1 and current > v2):
        return lca(root.left, v1, v2)
    elif(current < v1 and current < v2):
        return lca(root.right, v1, v2)
    else:
        return root

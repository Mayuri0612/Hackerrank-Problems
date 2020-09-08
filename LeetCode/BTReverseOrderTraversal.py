# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root is None:
            return root
    
        queue = []
        lis = []
        queue.append(root)
        while(len(queue) > 0):
            ans = []
            for _ in range(len(queue)):
                node = queue.pop(0)
                ans.append(node.val)
                if node.left is not None:
                    queue.append(node.left)
                if node.right is not None:
                    queue.append(node.right)
            lis.append(ans)
        lis.reverse()
        return(lis)

def helper(self, root, prev, result):
    if root is None: return
    self.helper(root.left, prev, result)
    if prev[0] and root.val <= prev[0].val:
        result[0] = False
        return
    prev[0] = root
    self.helper(root.right, prev, result)
    
    
def isValidBST(self, root):
    """
    :type root: TreeNode
    :rtype: bool
    """
    prev = [None]  
    result = [True]
    self.helper(root, prev, result)
    return result[0]
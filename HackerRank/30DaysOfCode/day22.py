   
def getHeight(self,root):
    if root is None or (root.left is None and root.right is None):
        return 0
    return 1 + max(self.getHeight(root.right), self.getHeight(root.left))

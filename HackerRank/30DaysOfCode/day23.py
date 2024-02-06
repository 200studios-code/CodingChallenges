
def levelOrder(self,root):
    inorder = ''
    queue = []
    node = root
    queue.append(node)
    while len(queue) > 0:
        node = queue.pop(0)
        inorder += (str(node.data) + ' ')
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    print(inorder)

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def inorderTraversal(root):
    result = []

    def traverse(node):
        if node:
            traverse(node.left)
            result.append(node.val)
            traverse(node.right)

    traverse(root)
    return result

# Приклад
tree_root = TreeNode(1, None, TreeNode(2, TreeNode(3)))
print(inorderTraversal(tree_root))  # Вивід: [1, 3, 2]

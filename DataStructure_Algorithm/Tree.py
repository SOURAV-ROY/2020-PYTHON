class TreeNode:
    def __init__(self, val):
        self.left = None
        self.right = None
        self.val = val


class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, val_2):
        if self.root in None:
            self.root = TreeNode(val_2)
        else:
            pass

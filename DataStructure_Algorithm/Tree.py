from DataStructure_Algorithm.Stack_Queue_BT_BST_DFS_BFS_TT import Queue
from DataStructure_Algorithm.BinaryTreePrinter import BinaryTreePrinter


class TreeNode:
    def __init__(self, val):
        self.left = None
        self.right = None
        self.val = val


class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, val_2):
        if self.root is None:
            self.root = TreeNode(val_2)
        else:
            nodes = Queue()
            nodes.enqueue(self.root)

            while True:
                checking_node = nodes.dequeue()
                if checking_node.left is None:
                    checking_node.left = TreeNode(val_2)
                    return
                elif checking_node.right is None:
                    checking_node.right = TreeNode(val_2)
                    return
                else:
                    nodes.enqueue(checking_node.left)
                    nodes.enqueue(checking_node.right)

    def __str__(self):
        tree_printer = BinaryTreePrinter()
        return tree_printer.get_tree_string(self.root)


my_tree = BinaryTree()
for c in ['a', 'b', 'c', 'd', 'e', 'f']:
    my_tree.insert(c)
    print(my_tree)

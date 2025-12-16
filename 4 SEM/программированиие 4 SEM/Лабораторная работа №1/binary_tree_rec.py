class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self, root):
        self.root = Node(root)

    def build_tree(self, height, root):
        if height == 0:
            return

        self.root.left = Node(root * 3)
        self.root.right = Node(root + 4)

        self.build_subtree(self.root.left, height - 1)
        self.build_subtree(self.root.right, height - 1)

    def build_subtree(self, node, height):
        if height == 0:
            return

        node.left = Node(node.value * 3)
        node.right = Node(node.value + 4)

        self.build_subtree(node.left, height - 1)
        self.build_subtree(node.right, height - 1)

    def print_tree(self):
        self._print_tree(self.root, 0)

    def _print_tree(self, node, level):
        if node is None:
            return

        print(" " * level + str(node.value))
        self._print_tree(node.left, level + 4)
        self._print_tree(node.right, level + 4)

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTreeNotRec:
    def __init__(self, root):
        self.root = Node(root)

    def build_tree(self, height, root):
        if height == 0:
            return

        queue = [(self.root, root)]
        for _ in range(height):
            next_level = []
            for node, value in queue:
                node.left = Node(value * 3)
                node.right = Node(value + 4)
                next_level.append((node.left, value * 3))
                next_level.append((node.right, value + 4))
            queue = next_level

    def print_tree(self):
        self._print_tree(self.root, 0)

    def _print_tree(self, node, level):
        if node is None:
            return

        print(" " * level + str(node.value))
        self._print_tree(node.left, level + 4)
        self._print_tree(node.right, level + 4)

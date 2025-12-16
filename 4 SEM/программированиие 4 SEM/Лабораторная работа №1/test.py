from binary_tree_rec import BinaryTree
from binary_tree_notrec import BinaryTreeNotRec

def test_binary_tree(root_value, tree_height):
    binary_tree_rec = BinaryTree(root_value)
    binary_tree_rec.build_tree(tree_height, root_value)
    print("Recursive Binary Tree:")
    binary_tree_rec.print_tree()

    binary_tree_notrec = BinaryTreeNotRec(root_value)
    binary_tree_notrec.build_tree(tree_height, root_value)
    print("Non-Recursive Binary Tree:")
    binary_tree_notrec.print_tree()

root_value = 2
tree_height = 5

test_binary_tree(root_value, tree_height)

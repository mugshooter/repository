import time
import matplotlib.pyplot as plt
from binary_tree_rec import BinaryTree
from binary_tree_notrec import BinaryTreeNotRec

def time_execution(build_tree_func, root_value, tree_height):
    start_time = time.time()
    build_tree_func(tree_height, root_value)
    end_time = time.time()
    return end_time - start_time

def test_binary_tree(root_value, tree_height):
    recursive_times = []
    non_recursive_times = []

    for height in tree_height:
        binary_tree_rec = BinaryTree(root_value)
        recursive_time = time_execution(binary_tree_rec.build_tree, root_value, height)
        recursive_times.append(recursive_time)

        binary_tree_notrec = BinaryTreeNotRec(root_value)
        non_recursive_time = time_execution(binary_tree_notrec.build_tree, root_value, height)
        non_recursive_times.append(non_recursive_time)

    plt.figure(figsize=(10, 6))
    plt.plot(tree_height, recursive_times, label='Рекурсивный метод')
    plt.plot(tree_height, non_recursive_times, label='Нерекурсивный метод')
    plt.xlabel('Высота дерева')
    plt.ylabel('Время выполнения (с)')
    plt.title('Время выполнения vs. Высота дерева')
    plt.legend()
    plt.grid(True)
    plt.show()

root_value = 2
tree_heights = [10, 20, 30, 40, 50]

test_binary_tree(root_value, tree_heights)

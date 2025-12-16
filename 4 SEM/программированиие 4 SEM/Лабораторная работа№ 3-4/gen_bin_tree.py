from exceptions import BinaryTreeException, HeightSubZeroException, InvalidRootArgumentException

import logging

gen_bin_tree_logger = logging.getLogger(__name__ + '.gen_bin_tree')
gen_bin_tree_logger.setLevel(logging.INFO)  # Устанавливаем уровень логгирования для этого логгера

console_handler = logging.StreamHandler()
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(funcName)s - %(message)s')
console_handler.setFormatter(formatter)
gen_bin_tree_logger.addHandler(console_handler)

def gen_bin_tree_recursive(height: int, root: int):
    try:
        gen_bin_tree_logger.info(f"Generating binary tree recursively with height {height} and root {root}")

        if height < 0:
            raise HeightSubZeroException('Высота дерева не может быть меньше нуля')

        if root < 0:
            raise InvalidRootArgumentException('Неправильно задан аргумент root')

        tree = {str(root): []}
        left_func = lambda root: root + 3
        right_func = lambda root: root * 2

        if height == 0:
            return tree
        else:
            l_l = left_func(root)
            r_l = right_func(root)
            gen_bin_tree_logger.debug(f"Left leaf: {l_l}, Right leaf: {r_l}")
            a = gen_bin_tree_recursive(root=l_l, height=height - 1)
            tree[str(root)].append(a)
            b = gen_bin_tree_recursive(root=r_l, height=height - 1)
            tree[str(root)].append(b)
        return tree
    except BinaryTreeException as e:
        gen_bin_tree_logger.error(f"Binary tree exception: {e}")

def gen_bin_tree_non_recursive(height: int, root: int):
    try:
        gen_bin_tree_logger.info(f"Generating binary tree non-recursively with height {height} and root {root}")

        if height < 0:
            raise HeightSubZeroException('Высота дерева не может быть меньше нуля')

        if root < 0:
            raise InvalidRootArgumentException('Неправильно задан аргумент root')

        tree = {str(root): []}
        left_func = lambda root: root + 3
        right_func = lambda root: root * 2

        stack = [(root, height, tree)]

        while stack:
            node, height, subtree = stack.pop()

            if height == 0:
                continue

            left_leaf = left_func(node)
            right_leaf = right_func(node)

            left_subtree = {str(left_leaf): []}
            subtree[str(node)].append(left_subtree)

            right_subtree = {str(right_leaf): []}
            subtree[str(node)].append(right_subtree)

            stack.append((left_leaf, height - 1, left_subtree))
            stack.append((right_leaf, height - 1, right_subtree))

        return tree
    except BinaryTreeException as e:
        gen_bin_tree_logger.error(f"Binary tree exception: {e}")

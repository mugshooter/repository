from exceptions import BinaryTreeException, HeightSubZeroException, InvalidRootArgumentException
from gen_bin_tree import gen_bin_tree_recursive, gen_bin_tree_non_recursive
import pprint as pp
import logging

main_logger = logging.getLogger(__name__ + '.main')
main_logger.setLevel(logging.INFO)  

console_handler = logging.StreamHandler()
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(funcName)s - %(message)s')
console_handler.setFormatter(formatter)
main_logger.addHandler(console_handler)

def main():
    try:
        main_logger.info("Starting the main function")
        t_recursive = gen_bin_tree_recursive(height=-1, root=5)
        t_non_recursive = gen_bin_tree_non_recursive(height=3, root=5)
        pp.pprint(t_recursive)
        pp.pprint(t_non_recursive)
    except HeightSubZeroException as e:
        main_logger.error(f"HeightSubZeroException: {e}")
        h = int(input("Height: "))
        t_recursive = gen_bin_tree_recursive(height=h, root=5)
        t_non_recursive = gen_bin_tree_non_recursive(height=h, root=5)
        pp.pprint(t_recursive)
        pp.pprint(t_non_recursive)

if __name__ == '__main__':
    main()

from goit_algo_hw7_tree_base import insert


def get_min_value(node):
    current = node
    while current.left is not None:
        current = current.left
    return current.key


if __name__ == '__main__':
    # Driver program to test the above functions
    root = None
    keys = [10, 20, 30, 25, 28, 27, -1]

    for key in keys:
        root = insert(root, key)

    print(get_min_value(root))

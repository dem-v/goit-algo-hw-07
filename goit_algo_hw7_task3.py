from goit_algo_hw7_tree_base import insert


def get_sum(node):
    if not node:
        return 0
    return node.key + get_sum(node.left) + get_sum(node.right)


if __name__ == '__main__':
    # Driver program to test the above functions
    root = None
    keys = [10, 20, 30, 25, 28, 27, -1]

    for key in keys:
        root = insert(root, key)

    print(get_sum(root))
    
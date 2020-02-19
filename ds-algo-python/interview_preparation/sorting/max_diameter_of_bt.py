class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def __get_height(node: Node):
    if node is None:
        return 0
    return 1 + max(__get_height(node.left), __get_height(node.right))


def __get_diameter(root: Node):
    if root is None:
        return 0
    l_height = __get_height(root.left)
    r_height = __get_height(root.right)

    return max(l_height + r_height + 1, max(__get_diameter(root.left), __get_diameter(root.right)))


if __name__ == '__main__':
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    print("Diameter of given binary tree is %d" % (__get_diameter(root)))


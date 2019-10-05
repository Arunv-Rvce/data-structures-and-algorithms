class Node:
    def __init__(self, item: int):
        self.item: int = item
        self.left: Node = None
        self.right: Node = None
        self.height: int = 1
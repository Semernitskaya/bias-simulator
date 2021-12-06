from binarytree import tree, bst, heap, NodeTypeError
from binarytree import Node


class Info:
    def __init__(self, age):
        self.age = age


class BiasNode(Node):
    def __init__(self, left=None, right=None, info=None):
        super().__init__(1, left, right)
        # self.val = "e"


root = BiasNode()
root.left = BiasNode()
root.right = BiasNode()
root.left.right = BiasNode()

print(root)
print(root.left.right)

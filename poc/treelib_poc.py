from treelib import Node, Tree


class Info:
    def __init__(self, age):
        self.age = age


info = Info(12)
print(info)

tree = Tree()
tree.create_node(info, "harry")  # root node
tree.create_node("Jane", "jane", parent="harry")
tree.create_node("Bill", "bill", parent="harry")
tree.create_node("Diane", "diane", parent="jane")
tree.create_node("Mary", "mary", parent="diane")
tree.create_node("Mark", "mark", parent="jane")

tree.show()

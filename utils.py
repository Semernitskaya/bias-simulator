from anytree import NodeMixin, RenderTree


KIND_A = "A"
KIND_C = "C"


class Person(NodeMixin):  # Add Node feature
    def __init__(self, kind, biased=False, parent=None, children=None):
        self.kind = kind
        self.age = 0
        self.biased = biased
        self.parent = parent
        if children:
            self.children = children


def calculate_max_descendants(tree_height):
    return pow(2, tree_height + 1) - 2


# TODO: add unbounded option
def add_person(root, person, max_tree_height):
    if len(root.descendants) > calculate_max_descendants(max_tree_height):
        return False
    if len(root.children) < 2:
        if root.biased and person.kind == KIND_C:
            return False
        else:
            root.children += (person,)
            return True
    elif len(root.children[0].descendants) < len(root.children[1].descendants):
        return True if add_person(root.children[0], person, max_tree_height - 1) else add_person(root.children[1], person, max_tree_height - 1)
    else:
        return True if add_person(root.children[1], person, max_tree_height - 1) else add_person(root.children[0], person, max_tree_height - 1)


def delete_conditioned(node, condition, comparator=lambda node1, node2: max(node1.kind, node2.kind)):
    pass


def print_tree(root):
    for pre, fill, node in RenderTree(root):
        treestr = u"%s%s(%s)" % (pre, node.kind, node.biased)
        print(treestr.ljust(20), node.age)


def add_tree_stat(root, stat):
    for _, _, node in RenderTree(root):
        if node.kind in stat:
            stat[node.kind] = stat[node.kind] + 1
        else:
            stat[node.kind] = 1


def add_array_stat(array, stat):
    for person in array:
        if person.kind in stat:
            stat[person.kind] = stat[person.kind] + 1
        else:
            stat[person.kind] = 1


def size(root):
    return len(root.descendants) + 1

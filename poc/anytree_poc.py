import random

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

generation_size = 5
biased_percent = 20
retirement_age = 3
max_tree_height = 2
generations_count = 9

pool = []
companies = []
current_generation = 0


def init():
    pass


def next_person():
    if random.randrange(2) == 0:
        kind = KIND_A
    else:
        kind = KIND_C
    if random.randrange(100) < biased_percent:
        biased = True
    else:
        biased = False
    return Person(kind, biased)


def max_descendants():
    return pow(2, max_tree_height + 1) - 2


def add_person(root, person):
    if len(root.descendants) == max_descendants():
        return False
    if len(root.children) < 2:
        root.children += (person,)
        return True
    elif len(root.children[0].descendants) < len(root.children[1].descendants):
        return add_person(root.children[0], person)
    else:
        return add_person(root.children[1], person)


for current_generation in range(generations_count):
    if current_generation == 0:
        for i in range(generation_size):
            companies.append(next_person())
    else:

        # increment age
        for company in companies:
            for pre, fill, node in RenderTree(company):
                node.age += 1
        # new generation
        for i in range(generation_size):
            pool.append(next_person())

        for person in list(pool):
            if add_person(min(companies, key=lambda c: len(c.descendants)), person):
                pool.remove(person)


    print(f"Generation {current_generation} ================================")
    for company in companies:
        for pre, fill, node in RenderTree(company):
            treestr = u"%s%s" % (pre, node.kind)
            print(treestr.ljust(8), node.age)

print("No company: " + str(len(pool)))




















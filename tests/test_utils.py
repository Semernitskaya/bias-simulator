from unittest import TestCase

from utils import Person, print_tree, add_person, delete_conditioned


def create_tree(letters):
    root = Person(letters[0])
    for i in range(1, len(letters)):
        add_person(root, Person(letters[i]), 1000)
    return root


class Test(TestCase):

    def test_delete_conditioned(self):
        tree = create_tree(['1', '2'])
        delete_conditioned(tree, lambda node: node.kind == '1')
        print_tree(tree)

        tree = create_tree(['1', '2'])
        delete_conditioned(tree, lambda node: node.kind == '2')
        print_tree(tree)

        tree = create_tree(['1', '2', '3'])
        delete_conditioned(tree, lambda node: node.kind == '2')
        print_tree(tree)

        tree = create_tree(['1', '2', '3'])
        delete_conditioned(tree, lambda node: node.kind == '3')
        print_tree(tree)

        tree = create_tree(['1', '2', '3'])
        delete_conditioned(tree, lambda node: node.kind == '1')
        print_tree(tree)

        tree = create_tree(['1', '2', '2'])
        delete_conditioned(tree, lambda node: node.kind == '2')
        print_tree(tree)

        tree = create_tree(['1', '2', '1'])
        delete_conditioned(tree, lambda node: node.kind == '1')
        print_tree(tree)
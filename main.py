import random

from anytree import RenderTree

from utils import Person, add_person, print_tree, add_stat, KIND_A, KIND_C, calculate_max_descendants

generation_size = 5
biased_percent = 20
retirement_age = 3
max_tree_height = 2
generations_count = 9
max_descendants = calculate_max_descendants(max_tree_height)

pool = []
companies = []
current_generation = 0


def next_person():
    kind = KIND_A if random.randrange(2) == 0 else KIND_C
    biased = kind == KIND_A and random.randrange(100) < biased_percent
    return Person(kind, biased)


for current_generation in range(generations_count):
    if current_generation == 0:
        for i in range(generation_size):
            companies.append(next_person())
    else:

        # increment age
        for company in companies:
            for pre, fill, node in RenderTree(company):
                node.age += 1

        # delete retired
        # for company in companies:
        #     delete_conditioned(company)

        # new generation
        for i in range(generation_size):
            pool.append(next_person())

        smallest_company = min(companies, key=lambda c: len(c.descendants))
        while len(smallest_company.descendants) < max_descendants and len(pool) > 0:
            person_added = False
            for person in list(pool):
                if add_person(smallest_company, person):
                    pool.remove(person)
                    person_added = True
                    break
            smallest_company = min(companies, key=lambda c: len(c.descendants))

    # print(f"Generation {current_generation} ================================")
    # for company in companies:
    #     print_tree(company)

print(f"Generation {current_generation} ================================")
stat = {}
for company in companies:
    print_tree(company)
    add_stat(company, stat)

print("No company: " + str(len(pool)))
print("In company: " + str(stat))

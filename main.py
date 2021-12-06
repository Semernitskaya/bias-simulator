import random
from functools import reduce

from anytree import RenderTree

from utils import Person, add_person, print_tree, add_tree_stat, KIND_A, KIND_C, calculate_max_descendants, \
    add_array_stat, Stat

generation_size = 10
biased_percent = 80
retirement_age = 3
max_tree_height = 7
generations_count = 300
max_descendants = calculate_max_descendants(max_tree_height)

pool = []
companies = []
current_generation = 0


def next_person():
    kind = KIND_A if random.randrange(2) == 0 else KIND_C
    biased = kind == KIND_A and random.randrange(100) < biased_percent
    return Person(kind, biased)


for current_generation in range(generations_count):
    print(f"Generation: {current_generation}")
    if current_generation == 0:
        for i in range(generation_size):
            companies.append(next_person())
    else:

        # increment age
        for company in companies:
            for pre, fill, node in RenderTree(company):
                node.age += 1
        # TODO: delete retired
        # delete retired
        # for company in companies:
        #     delete_conditioned(company)

        # new generation
        for i in range(generation_size):
            pool.append(next_person())

        # TODO: performance ???
        temp_companies = list(companies)
        smallest_company = min(temp_companies, key=lambda c: len(c.descendants))
        while len(smallest_company.descendants) < max_descendants and len(pool) > 0:
            person_added = False
            for person in list(pool):
                if add_person(smallest_company, person, max_tree_height):
                    pool.remove(person)
                    person_added = True
                    break
            if not person_added:
                temp_companies.remove(smallest_company)
            if len(temp_companies) == 0:
                break
            smallest_company = min(temp_companies, key=lambda c: len(c.descendants))


print(f"Generation {current_generation} ================================")
company_stat = {KIND_A: Stat(), KIND_C: Stat()}
for company in companies:
    print_tree(company)
    add_tree_stat(company, company_stat, max_tree_height)

pool_stat = {KIND_A: Stat(), KIND_C: Stat()}
add_array_stat(pool, pool_stat)

print(f"Max descendants: {max_descendants * generation_size}")
print(f"Actual descendants: {reduce(lambda res, c: res + len(c.descendants), companies, 0)}")
print(f"No company: A: {pool_stat[KIND_A]}, C: {pool_stat[KIND_C]}")
print(f"In company: A: {company_stat[KIND_A]}, C: {company_stat[KIND_C]}")

import random

from anytree import RenderTree

from utils import Person, add_person, print_tree, add_tree_stat, KIND_A, KIND_C, calculate_max_descendants, \
    add_array_stat

generation_size = 1
biased_percent = 50
retirement_age = 3
max_tree_height = 6
generations_count = 200
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

        # delete retired
        # for company in companies:
        #     delete_conditioned(company)

        # new generation
        for i in range(generation_size):
            pool.append(next_person())

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
company_stat = {KIND_A: 0, KIND_C: 0}
for company in companies:
    print_tree(company)
    add_tree_stat(company, company_stat)

pool_stat = {KIND_A: 0, KIND_C: 0}
add_array_stat(pool, pool_stat)

print(f"Max descendants: {max_descendants}")
print(f"Actual descendants: {len(companies[0].descendants)}")
print(f"No company: A: {pool_stat[KIND_A]}, C: {pool_stat[KIND_C]}")
print(f"In company: A: {company_stat[KIND_A]}, C: {company_stat[KIND_C]}")

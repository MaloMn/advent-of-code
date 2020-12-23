from utils import get_lines
import re


def are_elements_in_list(array, *args) -> bool:
    for a in args:
        if a not in array:
            return False
    return True


def get_foods(f):
    output = []
    for line in f:
        line = line.split('(contains')
        ingredients = re.findall(r'\w+', line[0])
        allergies = re.findall(r'\w+', line[1])
        output.append([ingredients, allergies])
    return output


def find_impossible_foods(foods):
    output = set()
    for food in foods:
        ingr = food[0]
        allergies = food[1]
        impossibles = set(ingr)
        print(impossibles)
        for f in foods:
            if f != food and are_elements_in_list(f[1], *allergies):
                impossibles.difference(set(f[0]))
                print('a', impossibles, f[1])

        output.union(impossibles)


if __name__ == "__main__":
    data = get_lines('allergens.txt')
    foods = get_foods(data)
    print(foods)

    print(find_impossible_foods(foods))


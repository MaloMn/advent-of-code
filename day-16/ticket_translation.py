from utils import get_lines
from typing import Dict, List
import re
from copy import deepcopy


def collect_fields(f):
    output: Dict = dict()
    for line in f:
        name = re.findall(r'.*:', line)[0]
        name = name[:len(name) - 1]
        ranges = [int(a) for a in re.findall(r'\d+', line)]
        output[name] = ranges
    return output


def collect_tickets(f):
    output: List = []
    for line in f:
        values = [int(a) for a in re.findall(r'\d+', line)]
        output.append(values)
    return output


def is_in_ranges(value, *args):
    in_range = False
    for a, b in zip(args[::2], args[1::2]):
        if a <= value <= b:
            in_range = True
            break
    return in_range


def remove_invalid_tickets(nearby, f):
    indexes = []
    for j, tick in enumerate(nearby):
        for n in tick:
            is_correct = False
            for ranges in f.values():
                if is_in_ranges(n, *ranges):
                    is_correct = True
                    break

            if not is_correct:
                indexes.append(j)

    return [a for i, a in enumerate(nearby) if i not in indexes]


def fields_count(f):
    left_names = []
    for b in f:
        if len(b) > 1:
            left_names += b

    for name in list(set(left_names)):
        if left_names.count(name) == 1:
            return name

    return None


if __name__ == "__main__":
    data = get_lines("ticket.txt")

    # Collect ranges
    end = data.index('')
    fields = collect_fields(data[:end])
    print(len(fields.keys()))

    # Collect my ticket
    data = data[end + 2:]
    my_ticket = collect_tickets(data[:1])[0]

    # Collect nearby tickets
    data = data[3:]
    nearby_tickets = collect_tickets(data)

    # Remove invalid tickets
    nearby_tickets = remove_invalid_tickets(nearby_tickets, fields)

    # Work out what column is what
    fields_matrix = []
    for i in range(len(fields.keys())):
        fields_matrix.append(deepcopy(list(fields.keys())))

    for ticket in nearby_tickets:
        for i, nb in enumerate(ticket):
            column_fields = fields_matrix[i]
            for field in column_fields:
                if not is_in_ranges(nb, *fields[field]):
                    fields_matrix[i].remove(field)

            if len(fields_matrix[i]) == 1:
                name = fields_matrix[i][0]
                for k in range(len(fields_matrix)):
                    if k != i:
                        try:
                            fields_matrix[k].remove(name)
                        except ValueError:
                            pass

    while True:
        name = fields_count(fields_matrix)
        if name is None:
            break

        for i in range(len(fields_matrix)):
            if fields_matrix[i].count(name) > 1:
                while fields_matrix[i].count(name) > 0:
                    fields_matrix[i].remove(name)
            elif fields_matrix[i].count(name) == 1:
                fields_matrix[i] = [name]

    fields_names = [a[0] for a in fields_matrix]
    print(fields_names)

    product = 1
    for key, value in zip(fields_names, my_ticket):
        if 'departure' in key:
            print(key, value)
            product *= value
    print(product)

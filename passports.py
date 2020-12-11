
passports = []
with open('passports.txt', 'r') as f:
    p = dict()
    while True:
        line = f.readline()

        if line == '\n' or line == '':
            passports.append(p)
            p = dict()
        else:
            line = line.replace('\n', '')
            line = line.split(' ')
            line = [a.split(':') for a in line]
            # print(line)
            line = [(key, value[:len(value)]) for key, value in line]
            p.update(line)

        if line == '':
            break


def _is_int_in_range(nb, a, b) -> bool:
    try:
        return a <= int(nb) <= b
    except ValueError:
        return False


def _is_str_composed_of(word, letters) -> bool:
    for letter in word:
        if letter not in letters:
            return False
    return True


def is_passport_valid(passport) -> bool:
    if len(passport) in [7, 8] and set(passport.keys()).intersection(needed) == needed:
        condition = True
        # Birth Year, four digits; at least 1920 and at most 2002
        condition &= _is_int_in_range(passport['byr'], 1920, 2002)

        # Issue Year, four digits; at least 2010 and at most 2020
        condition &= _is_int_in_range(passport['iyr'], 2010, 2020)

        # Expiration Year, four digits; at least 2020 and at most 2030
        condition &= _is_int_in_range(passport['eyr'], 2020, 2030)

        # Hair Color, a # followed by exactly six characters 0-9 or a-f
        condition &= len(passport['hcl']) == 7 and passport['hcl'][0] == '#'
        condition &= _is_str_composed_of(passport['hcl'][1:], [str(i) for i in range(10)] + ['a', 'b', 'c', 'd', 'e', 'f'])

        # Eye Color, exactly one of: amb blu brn gry grn hzl oth
        condition &= passport['ecl'] in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']

        # Passport ID, a nine-digit number, including leading zeroes
        condition &= _is_str_composed_of(passport['pid'], [str(i) for i in range(10)]) and len(passport['pid']) == 9

        # Height, a number followed by either cm or in:
        unit = passport['hgt'][len(passport['hgt']) - 2:]
        if unit == 'cm':
            # If cm, the number must be at least 150 and at most 193
            condition &= _is_int_in_range(passport['hgt'][:3], 150, 193)
        elif unit == 'in':
            # If in, the number must be at least 59 and at most 76.
            condition &= _is_int_in_range(passport['hgt'][:2], 59, 76)
        else:
            return False

        return condition


valid = 0
needed = {'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'}
for p in passports:
    if is_passport_valid(p):
        valid += 1

print(valid)

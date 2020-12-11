from utils import get_lines, product


def builtin_voltage(volts):
    volts.sort()
    volts = [0] + volts
    one_jolt, three_jolt = 0, 0
    for i in range(1, len(volts)):
        # print(volts[i-1], volts[i])
        if volts[i] - volts[i-1] > 3:
            return volts[i-1]

        if volts[i] - volts[i-1] == 1:
            one_jolt += 1
        elif volts[i] - volts[i-1] == 3:
            three_jolt += 1

    return one_jolt, three_jolt + 1


def fibonacci(n, table=[]):
    while len(table) < n+1:
        table.append(0)
    # base case
    if n <= 1:
        return n
    # recursive case
    else:
        if table[n-1] == 0:
            table[n-1] = fibonacci(n-1)

        if table[n-2] == 0:
            table[n-2] = fibonacci(n-2)

        table[n] = table[n-2] + table[n-1]
    return table[n]


def arrangements(volts, i=0) -> int:
    volts.sort()
    volts = [0] + volts
    output = 1
    i = 1
    a = 1
    while i < len(volts):
        if volts[i] - volts[i - 1] == 1:
            a += 1
        elif a > 1:
            output *= fibonacci(a + 1) - 1
            # print('a', a, fibonacci(a + 1) - 1)
            a = 1
        i += 1

    if a > 1:
        output *= fibonacci(a + 1) - 1
        # print('a', a, fibonacci(a + 1) - 1)

    return output


if __name__ == "__main__":
    data = get_lines('adaptater-array')
    data = [int(a) for a in data]
    # Removing doubles and sorting
    data = list(set(data))
    print(data)
    result = builtin_voltage(data)
    print(product(result))

    print(arrangements(data))

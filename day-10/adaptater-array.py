from utils import get_lines, product


def builtin_voltage(volt):
    volt.sort()
    volt = [0] + volt
    one_jolt, three_jolt = 0, 0
    for i in range(1, len(volt)):
        # print(volt[i-1], volt[i])
        if volt[i] - volt[i-1] > 3:
            return volt[i-1]

        if volt[i] - volt[i-1] == 1:
            one_jolt += 1
        elif volt[i] - volt[i-1] == 3:
            three_jolt += 1

    return one_jolt, three_jolt + 1


def arrangements(volts, i=0) -> int:
    # print("arrangements(volts, {})".format(volts[i]))
    output = 0
    j = i + 1
    while j < len(volts) and volts[j] - volts[i] <= 3:
        output += arrangements(volts, j)
        j += 1

    output = 1 if output == 0 else output
    # print("--> arrangements(volts, {}) returned {}".format(volts[i], output))
    return output


if __name__ == "__main__":
    data = get_lines('adaptater-array')
    data = [int(a) for a in data]
    # Removing doubles and sorting
    data = list(set(data))
    data.sort()
    print(data)
    # result = builtin_voltage(data)
    # print(product(result))

    print(arrangements(data))

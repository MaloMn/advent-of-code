from utils import get_lines, product


def extended_euclide(a, b):
    s, old_s = 0, 1
    r, old_r = b, a

    while r != 0:
        quotient = old_r // r
        old_r, r = r, old_r - quotient * r
        old_s, s = s, old_s - quotient * s

    if b != 0:
        bezout_t = int((old_r - old_s * a) / b)
    else:
        bezout_t = 0

    # print("{}{}x{} {} {}x{} = {}".format("-" if a*old_s < 0 else "", abs(a), abs(old_s),
    #                                      "-" if b*bezout_t < 0 else "+", abs(b), abs(bezout_t), old_r))
    return old_s, bezout_t


def chinese_remainder(a, n):
    N = product(n)

    output = 0
    for ni, ai in zip(n, a):
        _, s = extended_euclide(ni, N//ni)
        output += ai*s*N//ni
        # print(ai, s, N//ni)

    return output % N


def draw(start, bus_ids):
    output = 'time\t' + '\t'.join(bus_ids) + '\n'
    for i in range(start, start + 10):
        line = str(i)
        for bus in bus_ids:
            try:
                if i % int(bus) == 0:
                    line += '\t0'
                else:
                    line += '\t.'
            except:
                line += '\t.'
        output += line + '\n'
    print(output)


if __name__ == "__main__":
    _, ids = get_lines("shuttle.txt")
    ids = ids.split(",")
    # draw(3417, ids)

    rests = [-i for i in range(len(ids)) if ids[i] != 'x']
    ids = [int(i) for i in ids if i != 'x']
    print(rests, ids)
    print(chinese_remainder(rests, ids))
    # print(chinese_remainder([2, 3, 2], [3, 5, 7]))


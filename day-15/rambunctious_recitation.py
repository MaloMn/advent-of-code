from utils import get_lines


if __name__ == "__main__":
    data = get_lines('recitation.txt')
    start_nb = data[0].split(',')
    start_nb = [int(a) for a in start_nb]

    previous_nb = start_nb[-1]
    mem = {a: [i + 1] for i, a in enumerate(start_nb)}

    goal = 30000000
    for i in range(len(start_nb) + 1, goal + 1):
        # print(i, previous_nb, mem)
        if len(mem[previous_nb]) == 1:
            previous_nb = 0
        else:
            previous_nb = mem[previous_nb][-1] - mem[previous_nb][-2]

        if previous_nb in mem.keys():
            mem[previous_nb].append(i)
        else:
            mem[previous_nb] = [i]

        if i % 1000000 == 0:
            print(i)

    print(previous_nb)

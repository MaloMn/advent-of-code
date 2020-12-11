with open('trees.txt', 'r') as f:
    data = f.readlines()

data = [list(line)[:len(list(line)) - 1] for line in data]

result = 1
for down, right in zip([1, 1, 1, 1, 2], [1, 3, 5, 7, 1]):
    x, y = 0, 0
    nb_trees = 0

    while x < len(data):
        if data[x][y] == '#':
            nb_trees += 1

        x += down
        y += right

        if y >= len(data[0]):
            y -= len(data[0])

    result *= nb_trees

print(result)

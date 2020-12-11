data = []
first = True
with open('forms.txt', 'r') as f:
    while True:
        line = f.readline()
        if line == '':
            break
        line = line.replace('\n', '')
        if line == '':
            first = True
        else:
            if first:
                data.append(set(list(line)))
                first = False
            else:
                data[-1] = data[-1].intersection(set(list(line)))

# print(data)
# data = [set(list(a)) for a in data]
print(sum([len(a) for a in data]))

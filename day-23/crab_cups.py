class Cups:

    def __init__(self, order):
        self.order = order
        self.current = 0

    def get_next_three(self):
        print(self)
        if self.current == len(self.order) - 3:
            output = self.order[len(self.order) - 2:len(self.order)] + self.order[0]
        elif self.current == len(self.order) - 2:
            output = self.order[-1] + self.order[:2]
        elif self.current == len(self.order) - 1:
            output = self.order[:3]
        else:
            output = self.order[self.current + 1:self.current + 4]

        for i in output:
            self.order.remove(i)

        print('pick up:', ', '.join([str(a) for a in output]))
        return output

    def get_destination_cup(self):
        label = self.order[self.current] - 1
        while True:
            try:
                self.current = self.order.index(label)
                break
            except ValueError:
                label -= 1
                if label < min(self.order):
                    label = max(self.order)

        print('destination:', label)

    def place_three_cups(self, three):
        self.order = self.order[:self.current + 1] + three + self.order[self.current + 1:]

    def __str__(self):
        output = ''
        for o in self.order:
            if self.order[self.current] == o:
                output += ' (' + str(o) + ')'
            else:
                output += ' ' + str(o)

        output = 'cups:' + output
        return output


def move(order, n=100):
    cups = Cups(order)
    for i in range(n):
        nb = cups.get_next_three()
        cups.get_destination_cup()
        cups.place_three_cups(nb)
        print('\n')
    return cups.order


if __name__ == "__main__":
    numbers = list('389125467')
    numbers = [int(a) for a in numbers]
    print(move(numbers, n=10))





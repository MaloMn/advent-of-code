from utils import get_lines


def combat(decks) -> str:
    while len(decks['a']) > 0 and len(decks['b']) > 0:
        nb_a, nb_b = decks['a'].pop(0), decks['b'].pop(0)
        winner = 'a' if nb_a > nb_b else 'b'

        if winner == 'a':
            decks['a'] += [nb_a, nb_b]
        else:
            decks['b'] += [nb_b, nb_a]

    if len(decks['a']) > len(decks['b']):
        return 'a'
    return 'b'


def deck_to_hash(deck_a, deck_b):
    deck_a = hash(''.join([str(i) for i in deck_a]))
    deck_b = hash(''.join([str(i) for i in deck_b]))
    return hash(deck_a + deck_b)


def recursive_combat(decks) -> str:
    # print('NEW COMBAT', f"a: {decks['a']}, b: {decks['b']}")
    prev_decks = []
    while len(decks['a']) > 0 and len(decks['b']) > 0:

        if deck_to_hash(decks['a'], decks['b']) in prev_decks:
            # print('Situation encountered before.')
            return 'a'
        else:
            prev_decks.append(deck_to_hash(decks['a'], decks['b']))

            nb_a, nb_b = decks['a'].pop(0), decks['b'].pop(0)
            if nb_a <= len(decks['a']) and nb_b <= len(decks['b']):
                # Recursion
                winner = recursive_combat({'a': decks['a'][:nb_a], 'b': decks['b'][:nb_b]})
            else:
                winner = 'a' if nb_a > nb_b else 'b'

        if winner == 'a':
            decks['a'] += [nb_a, nb_b]
        else:
            decks['b'] += [nb_b, nb_a]

    if len(decks['a']) > len(decks['b']):
        return 'a'

    return 'b'


if __name__ == "__main__":
    data = get_lines("crab_combat.txt")
    data = [int(a) for a in data if 'Player' not in a and a != '']
    middle = len(data) // 2

    a, b = data[:middle], data[middle:]
    players = {'a': a, 'b': b}
    win = combat(players)
    print(f"Answer 1: {sum([(i + 1) * j for i, j in enumerate(players[win][::-1])])}")

    a, b = data[:middle], data[middle:]
    players = {'a': a, 'b': b}
    win = recursive_combat(players)
    print(f"Answer 2: {sum([(i + 1) * j for i, j in enumerate(players[win][::-1])])}")

import itertools
import datetime

def answer(x, y, z):

    permutations = set()
    cards = [x, y, z]

    for permutation in itertools.permutations(cards):
        try:
            datetime.datetime(permutation[2], permutation[0], permutation[1])
            permutations.add(permutation)
        except ValueError:
            # date is not valid, so it is not added to the list
            pass

    if len(permutations) > 1:
        return 'Ambiguous'
    else:
        date = permutations.pop()
        date_format = '{:0>2d}'
        return date_format.format(date[0]) + '/' +\
               date_format.format(date[1]) + '/' +\
               date_format.format(date[2])

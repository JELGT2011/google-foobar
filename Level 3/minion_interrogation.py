def answer(minions):

    # minion = [weight, numerator, denominator, success rate, original index]
    for minion in minions:
        minion.append(float(minion[1]) / minion[2])
        minion.append(minions.index(minion))

    best_ordering = sorted(minions, key=lambda minion: minion[0] / minion[3])

    return map(lambda minion: minion[4], best_ordering)
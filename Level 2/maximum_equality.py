def answer(x):

    average = sum(x) / len(x)
    overflow = 0

    for item in x:
        difference = item - average
        item -= difference
        overflow -= difference

    return len(x) + (overflow / average)




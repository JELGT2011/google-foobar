def answer(meetings):

    solution = []
    meetings.sort(key=lambda meeting: meeting[1])

    while len(meetings) > 0:
        optimal = meetings.pop(0)
        overlappings = []
        for meeting in meetings:
            # if this meeting starts after the optimal meeting, remove it
            if meeting[0] < optimal[1]:
                overlappings.append(meeting)

        for overlapping in overlappings:
            meetings.remove(overlapping)
        solution.append(optimal)

    return len(solution)

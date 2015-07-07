def topological_sort(topological_graph):
    lexicographical_ordering = []
    visited = []

    def visit(node):
        if node not in visited:
            visited.append(node)
            for child in topological_graph[node]:
                visit(child)
            lexicographical_ordering.append(node)

    for key in topological_graph:
        visit(key)

    return lexicographical_ordering

def answer(words):

    topological_graph = {}

    padding = ' '
    max_length = len(max(words, lambda word: len(word)))

    for i in range(len(words)):
        words[i] += padding * (max_length - len(words[i]))

    for i in range(len(words) - 1):
        common_prefix_length = 0
        while words[i][common_prefix_length] == words[i + 1][common_prefix_length]:
            common_prefix_length += 1

        if words[i][common_prefix_length] not in topological_graph.keys():
            topological_graph[words[i][common_prefix_length]] = []

        if words[i + 1][common_prefix_length]not in topological_graph.keys():
            topological_graph[words[i + 1][common_prefix_length]] = []

        topological_graph[words[i + 1][common_prefix_length]].append(words[i][common_prefix_length])

    lexicographical_ordering = topological_sort(topological_graph)

    return ''.join(lexicographical_ordering).replace(' ', '')

words = ["y", "z", "xy"]
print(answer(words))

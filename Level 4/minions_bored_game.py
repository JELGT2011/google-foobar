def answer(t, n):

    class Node(object):

        def __init__(self, data, **options):
            self.data = data
            self.valid = True if 0 <= self.data[1] <= n - self.data[0] else False
            self.visited = False
            self.leaf = True if self.data[0] == t else False
            if 'flow' in options:
                self.flow = options['flow']

    def construct_graph(current):

        for direction in range(-1, 2):
            child = Node([current.data[0] + 1, current.data[1] + direction])
            if child.valid:
                graph[current].append(child)
                if child not in graph:
                    graph[child] = []

                construct_graph(child)

    def find_valid_flow(root):
        frontier = [root]
        root.visited = True
        while len(frontier) > 0:
            current = frontier.pop(len(frontier) - 1)
            for child in graph[current]:
                if not child.visited:
                    frontier.insert(0, child)
                    child.visited = True

    root = Node([0, 0])

    graph = {
        root: []
    }

    construct_graph(root)
    # find_valid_flow(root)

    return t % 123454321


answer(6, 4)

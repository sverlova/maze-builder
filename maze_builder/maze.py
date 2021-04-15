class Maze:
    directions = [ [0, 2], [2, 0], [0, -2], [-2, 0] ]
    # 4 directions where to move in graph
    # will be used in building

    def __init__(self, n, m):
        self.size = (n, m)
        self.shape = (2 * n + 1, 2 * m + 1)
        # n is height, m is width
        self.graph = [ [ (i % 2) * (j % 2) for i in range(self.shape[1])] for j in range(self.shape[0]) ]
        # 0 for wall and 1 for path
        # initialized with full-filled maze
        # looks like this: (for size = (2, 3))
        # #######
        # # # # #
        # #######
        # # # # #
        # #######

    def build(self):
        self.graph = [ [ 0 if i * j == 0 or i == self.shape[1] - 1 or j == self.shape[0] - 1
                         or (i % 2 == 0 and j % 2 == 0) else 1
                         for i in range(self.shape[1])] for j in range(self.shape[0]) ]
        # empty maze
        self.graph[0][1] = self.graph[-1][-2] = 1


    def __str__(self):
        s = ''
        for line in self.graph:
            for symb in line:
                if symb == 0:
                    s += '#'
                # wall
                else:
                    s += ' '
                # path
            s += '\n'
        return s

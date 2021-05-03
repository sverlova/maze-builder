class Maze:
    directions = [ [0, 2], [2, 0], [0, -2], [-2, 0] ]
    # 4 directions where to move in graph
    # will be used in building

    def create_from_shape(self, n, m):
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

    def create_from_graph(self, lines):
        self.shape = (len(lines), len(lines[0]))
        self.size = (self.shape[0] // 2, self.shape[1] // 2)
        # n is height, m is width
        self.graph = [ [ int(lines[j][i] != '#') for i in range(self.shape[1])] for j in range(self.shape[0]) ]


    def __init__(self, n, m=None):
        if m == None:
            self.create_from_graph(n)
        else:
            self.create_from_shape(n, m)

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

    def get_lines(self):
        s = self.__str__()
        lines = [ s[i * (self.shape[1] + 1) : (i + 1) * (self.shape[1] + 1) - 1] for i in range(self.shape[0]) ]
        return lines

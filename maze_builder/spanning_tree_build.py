from maze_builder.maze import *
import random

class STMaze(Maze):
# uses Kruskal's algorithm with random edges' weights

    def get_parent(self, a):
        if self.parents[a[0]][a[1]] == a:
            return a
        else:
            self.parents[a[0]][a[1]] = self.get_parent(self.parents[a[0]][a[1]])
            return self.parents[a[0]][a[1]]

    def unite(self, a, b):
        a = self.get_parent(a)
        b = self.get_parent(b)
        if a == b:
            return False
        self.parents[a[0]][a[1]] = b
        return True


    def build(self):
        self.parents = [ [ (j, i) for i in range(self.shape[1]) ] for j in range(self.shape[0]) ]
        self.union = [ [ (j, i) for i in range(self.shape[1]) ] for j in range(self.shape[0]) ]
        # params for DSU

        edges = []
        for i in range(1, self.shape[0], 2):
            for j in range(1, self.shape[1], 2):
                for delta in Maze.directions[:2]:
                    x = i + delta[0]
                    y = j + delta[1]
                    if x > 0 and y > 0 and x < self.shape[0] and y < self.shape[1]:
                        edges.append( (random.randint(1, 10000), (i, j), (x, y)) )

        edges.sort()

        for edge in edges:
            x, y = edge[1:]
            if self.unite(x, y):
                self.graph[(x[0] + y[0]) // 2][(x[1] + y[1]) // 2] = 1

        self.graph[0][1] = self.graph[-1][-2] = 1

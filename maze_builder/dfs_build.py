from maze_builder.maze import *
import random

class DFSMaze(Maze):

    def dfs(self, i, j):
        if self.visited[i][j]:
            return
        self.visited[i][j] = True
        free_neighbours = []
        for delta in Maze.directions:
            x = i + delta[0]
            y = j + delta[1]
            if x > 0 and y > 0 and x < self.shape[0] and y < self.shape[1] and (not self.visited[x][y]):
                free_neighbours.append((x, y))
        while len(free_neighbours) > 0:
            _next = random.randint(0, len(free_neighbours) - 1)
            # choose where to go now
            free_neighbours[-1], free_neighbours[_next] = free_neighbours[_next], free_neighbours[-1]
            if not self.visited[free_neighbours[-1][0]][free_neighbours[-1][1]]:
                self.graph[(i + free_neighbours[-1][0]) // 2][(j + free_neighbours[-1][1]) // 2] = 1
                # take the wall between cells away
            self.dfs(*free_neighbours.pop())
            # go

    def build(self):
        self.visited = [ [ False for i in range(self.shape[1]) ] for j in range(self.shape[0]) ]
        self.dfs(1, 1)
        self.graph[0][1] = self.graph[-1][-2] = 1

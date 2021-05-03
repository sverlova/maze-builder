from maze_builder.maze import *

class MazeSolver(Maze):
    def dfs(self, i, j):
        if self.visited[i][j]:
            return False
        self.visited[i][j] = True
        good_way = (i == self.shape[0] - 1 and j == self.shape[1] - 2)
        for delta in Maze.directions:
            x = i + delta[0] // 2
            y = j + delta[1] // 2
            if x > 0 and y > 0 and x < self.shape[0] and y < self.shape[1] and (not self.visited[x][y]):
                if self.dfs(x, y):
                    good_way = True
                    break
        if good_way:
            self.solved[i][j] = 2
        return good_way

    def solve(self):
        self.solved = [ [ self.graph[j][i] for i in range(self.shape[1]) ] for j in range(self.shape[0]) ]
        self.visited = [ [ self.graph[j][i] == 0 for i in range(self.shape[1]) ] for j in range(self.shape[0]) ]
        self.dfs(0, 1)

    def __str__(self):
        s = ''
        for line in self.solved:
            for symb in line:
                if symb == 0:
                    s += '#'
                # wall
                elif symb == 1:
                    s += ' '
                # free space
                else:
                    s += '*'
            s += '\n'
        return s

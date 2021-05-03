from maze_builder.dfs_build import *
from maze_builder.spanning_tree_build import *
from maze_builder.maze_solver import *
from functools import wraps

def wrong_option():
    print('Wrong option. Please try again.')

def cycle(f):
    @wraps(f)
    def wrapper():
        while True:
            option = f()
            if type(option) != type(False) or option != False:
                return option
            wrong_option()
    return wrapper

@cycle
def get_maze_options():
    options = [1, 2]
    print('''
Choose option:
1. Create maze now
2. Read from file
    ''')
    option = int(input())
    if option in options:
        return option
    else:
        return False

@cycle
def choose_maze_type():
    options = [1, 2]
    print('''
Choose maze type:
1. DFS maze
2. Spanning tree maze
    ''')
    option = int(input())
    if option in options:
        return option
    else:
        return False

@cycle
def choose_shape():
    while True:
        print('Enter size of maze:')
        shape = list(map(int, input().split()))
        if len(shape) != 2 or shape[0] <= 0 or shape[1] <= 0:
            return False
        else:
            return shape

def build_maze(type, shape):
    maze = None
    if type == 1:
        maze = DFSMaze(*shape)
    elif type == 2:
        maze = STMaze(*shape)
    maze.build()
    return maze

def create_maze():
    type = choose_maze_type()
    if type == 0:
        exit()
    shape = choose_shape()
    return build_maze(type, shape)

def read_maze():
    print('Type filename:')
    filename = input()
    lines = []
    with open(filename, 'r') as f:
        for line in f:
            if line != '':
                lines.append(line[:-1])
    return Maze(lines)

def get_maze():
    option = get_maze_options()
    maze = None
    if option == 1:
        maze = create_maze()
    elif option == 2:
        maze = read_maze()
    print('Done!')
    return maze

@cycle
def choose_action_with_maze():
    options = [0, 1, 2, 3]
    print('''
Where to put a maze?
1. Print here
2. Save into file
3. Show solution
0. Nowhere. Exit
    ''')
    option = int(input())
    if option in options:
        return option
    else:
        return False

def actions_with_maze(maze):
    option = choose_action_with_maze()
    if option == 0: exit()
    elif option == 1:
        print(maze)
    elif option == 2:
        print('Enter file name:')
        filename = input()
        with open(filename, 'w') as f:
            f.write(maze.__str__())
    elif option == 3:
        solver = MazeSolver(maze.get_lines())
        solver.solve()
        print(solver)


def run():
    maze = get_maze()

    while True:
        actions_with_maze(maze)
        print('Something else?')

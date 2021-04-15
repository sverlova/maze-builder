from maze_builder.dfs_build import *
from maze_builder.spanning_tree_build import *

option = None
while True:
    print(
    '''Welcome to maze builder. Choose option:
    1. DFS maze
    2. Spanning tree maze
    0. Exit'''
    )
    option = int(input())
    if option == 0: exit()
    if option != 1 and option != 2:
        print('Wrong option. Please try again.')
    else:
        break
shape = None
while True:
    print('Enter size of maze:')
    shape = list(map(int, input().split()))
    if len(shape) != 2 or shape[0] <= 0 or shape[1] <= 0:
        print('Wrong option. Please try again.')
    else:
        break
maze = None
if option == 1:
    maze = DFSMaze(*shape)
elif option == 2:
    maze = STMaze(*shape)
maze.build()

print('Done!')

option = None
while True:
    print(
    '''Where to put a maze?
    1. Print here
    2. Save into file
    0. Nowhere. Exit'''
    )
    option = int(input())
    if option == 0: exit()
    if option != 1 and option != 2:
        print('Wrong option. Please try again.')
    else:
        if option == 1:
            print(maze)
        elif option == 2:
            print('Enter file name:')
            filename = input()
            with open(filename, 'w') as f:
                f.write(maze)
        print('Something else?')

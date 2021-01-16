import numpy as np
import astarmodule as astar
import greedymodule as greedy
import nodemodule as node


if __name__ == '__main__':  
    maze = [[1, 1, 1, 0, 1, 1, 1],
            [1, 0, 0, 0, 0, 1, 1],
            [1, 0, 1, 1, 0, 1, 1],
            [1, 0, 1, 0, 0, 0, 1],
            [1, 0, 0, 0, 1, 0, 1],
            [1, 0, 1, 0, 0, 0, 1],
            [1, 1, 1, 0, 1, 1, 1]]  

    
    start = [0, 3]; end = [6, 3]
    maze[start[0]][start[1]] = 0
    maze[end[0]][end[1]] = 0

    # print(path)
    path_astar = astar.astar_search(maze, start, end)
    path_greedy = greedy.greedy_search(maze, start, end)
    print('\n')
    print('\n'.join([''.join(["{:" ">3d}".format(item) for item in row]) 
      for row in maze]))
    print('\n')
    print('A-star Algorithm\n')
    print('\n'.join([''.join(["{:" ">3d}".format(item) for item in row]) 
      for row in path_astar]))
    print('\n')
    print('Greedy Algorithm\n')
    print('\n'.join([''.join(["{:" ">3d}".format(item) for item in row]) 
      for row in path_greedy]))
    print('\n')